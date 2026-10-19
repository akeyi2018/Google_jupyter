# udp_rtt_client.py
# PC A側で実行するRTT測定クライアント
# ポート: 60001

import socket
import time
import statistics

# =========================================================
# ★ 後で埋める：PC B（エコーサーバ）のIPアドレスを指定
# =========================================================
SERVER_IP = "192.168.1.100"   # ← PC BのIPアドレスに置き換える
PORT = 60001

COUNT = 10          # 測定回数
TIMEOUT = 1.0       # 応答待ちタイムアウト（秒）
INTERVAL = 0.2      # 各測定間の待機時間（秒）
BUFFER_SIZE = 4096

def main():
    rtts = []
    lost = 0

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(TIMEOUT)

        print(f"[Client] Target: {SERVER_IP}:{PORT}")
        print(f"[Client] Count={COUNT}, Timeout={TIMEOUT}s")

        for seq in range(COUNT):
            payload = f"ping-{seq}".encode("utf-8")

            # 送信直前の時刻を記録
            send_time = time.perf_counter()
            sock.sendto(payload, (SERVER_IP, PORT))

            try:
                data, addr = sock.recvfrom(BUFFER_SIZE)
                recv_time = time.perf_counter()

                rtt_ms = (recv_time - send_time) * 1000.0

                if data == payload:
                    rtts.append(rtt_ms)
                    print(f"[Client] seq={seq} RTT={rtt_ms:.3f} ms from {addr}")
                else:
                    print(f"[Client] seq={seq} payload mismatch: sent={payload!r}, recv={data!r}")

            except socket.timeout:
                lost += 1
                print(f"[Client] seq={seq} timeout (lost)")

            time.sleep(INTERVAL)

    # =========================================================
    # 統計表示
    # =========================================================
    print("\n===== Result =====")
    print(f"Sent: {COUNT}, Received: {len(rtts)}, Lost: {lost}")

    if rtts:
        print(f"Min RTT : {min(rtts):.3f} ms")
        print(f"Max RTT : {max(rtts):.3f} ms")
        print(f"Avg RTT : {statistics.mean(rtts):.3f} ms")

        if len(rtts) >= 2:
            print(f"Std Dev : {statistics.stdev(rtts):.3f} ms")
        else:
            print("Std Dev : N/A (need at least 2 samples)")

        loss_rate = lost / COUNT * 100.0
        print(f"Loss    : {loss_rate:.1f} %")
    else:
        print("No successful RTT samples.")

if __name__ == "__main__":
    main()
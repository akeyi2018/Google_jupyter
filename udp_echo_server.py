# udp_echo_server.py
# PC B側で実行するエコーサーバ
# ポート: 60001

import socket

PORT = 60001
BUFFER_SIZE = 4096

def main():
    # UDPソケットを作成
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # すべてのインターフェースで待ち受け
        sock.bind(("0.0.0.0", PORT))
        print(f"[Server] UDP echo server listening on 0.0.0.0:{PORT}")

        try:
            while True:
                data, addr = sock.recvfrom(BUFFER_SIZE)
                print(f"[Server] Received {len(data)} bytes from {addr}: {data!r}")
                # 受信データをそのまま返送
                sock.sendto(data, addr)
        except KeyboardInterrupt:
            print("\n[Server] Shutdown.")

if __name__ == "__main__":
    main()
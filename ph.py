import socket
import struct
import time

def traceroute():
    destination = input("Hedef IP veya Alan Adı Girin: ")
    try:
        dest_ip = socket.gethostbyname(destination)
        print(f"Hedef: {destination} [{dest_ip}]...")
    except socket.gaierror:
        print("Hedef çözümlenemedi. Lütfen doğru bir adres girin.")
        return
    
    max_hops = int(input("Maksimum Hop Sayısını (TTL) Girin: "))
    timeout = float(input("Zaman Aşımı Süresini (saniye) Girin: "))
    port = int(input("Port Numarasını Girin (Örn: 33434): "))
    
    ttl = 1
    while ttl <= max_hops:
        recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        
        recv_socket.settimeout(timeout)
        recv_socket.bind(("", port))
        send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        
        start_time = time.time()
        send_socket.sendto(b"", (destination, port))
        
        curr_addr = None
        curr_name = None
        try:
            _, curr_addr = recv_socket.recvfrom(512)
            curr_addr = curr_addr[0]
            try:
                curr_name = socket.gethostbyaddr(curr_addr)[0]
            except socket.herror:
                curr_name = "Hostname bulunamadı"
        except socket.error:
            pass
        finally:
            send_socket.close()
            recv_socket.close()
        
        elapsed_time = (time.time() - start_time) * 1000
        if curr_addr:
            print(f"{ttl}\tAdres: {curr_addr}\tHostname: {curr_name}\tGecikme: {elapsed_time:.2f} ms")
        else:
            print(f"{ttl}\t*\tZaman Aşımı.")
        
        ttl += 1
        if curr_addr == dest_ip:
            print("İzleme Tamamlandı.")
            break

if __name__ == "__main__":
    traceroute()

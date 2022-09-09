import socket

def send_msg(udp_socket, dest_ip, dest_port):
    # 从键盘获取数据
    send_data = input("请输入要发送的内容").encode("gbk")
    # 使用套接字收发数据
    udp_socket.sendto(send_data, (dest_ip, dest_port))

def recv_meg(udp_socket):
    # 接受发送回来的数据--如果没有数据发回来就会阻塞
    recev_data = udp_socket.recvfrom(1024)
    recev_mess = recev_data[0]
    recev_addr = recev_data[1]
    print(recev_mess.decode("gbk"), recev_addr)  # windows中是gbk编码

def main():
    #创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    """
        函数 socket.socket 创建一个 socket，该函数带有两个参数：
            Address Family：可以选择 AF_INET（用于 Internet 进程间通信） 或者 AF_UNIX（用于同一台机器进程间通信）,实际工作中常用AF_INET
            Type：套接字类型，可以是 SOCK_STREAM（流式套接字，主要用于 TCP 协议）或者 SOCK_DGRAM（数据报套接字，主要用于 UDP 协议）
        """

    # 获取对方的ip以及端口
    dest_ip = input("请输入对方的ip")
    dest_port = int(input("请输入对方的端口"))
    #绑定一个本地信息--发送方可以不绑定端口，但是如果想要接受数据的话必须绑定端口
    localaddr = ("", 4444)
    udp_socket.bind(localaddr)

    while True:
        print("------半双工聊天器------")#半双工也有好处，防止被恶意无限攻击，导致系统瘫痪
        print("1:发送数据")
        print("2:接受数据")
        print("0:退出")
        act = int(input("请输入操作指令："))
        if act == 1:
            send_msg(udp_socket, dest_ip, dest_port)
        elif act == 2:
            recv_meg(udp_socket)
        elif act == 0:
            break
        else:
            print("输入有误请重新输入!")
    #关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.Net.Sockets;

namespace ServerRaspiBot
{
    class Program
    {
        static void Main(string[] args)
        {
            Socket sck = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);

            sck.Bind(new IPEndPoint(IPAddress.Parse("192.168.178.112"), 8001));
            sck.Listen(0);

            Socket acc = sck.Accept();
            byte[] buffer = Encoding.Default.GetBytes("Hello World");
            acc.Send(buffer, 0, buffer.Length, 0);
            
            buffer = new byte[255];

            int rec = acc.Receive(buffer, 0, buffer.Length, 0);

            Array.Resize(ref buffer, rec);

            Console.WriteLine("Received: {0}", Encoding.Default.GetString(buffer));

            sck.Close();
            acc.Close();
        }
    }
}

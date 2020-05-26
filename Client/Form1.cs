using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using WebSocketSharp;

namespace RaspiBot
{
    public partial class Form1 : Form
    {
        string direction = "empty";
        string moved = "start";
        
        public Form1()
        {
            InitializeComponent();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (direction != moved || direction == "empty")
            {
                webSocket(direction);
            }
                
        }

        private void webSocket(string test)
        {
            using (var ws = new WebSocket("ws://31.16.67.247:80"))
            {
                ws.OnOpen += (sender, e) => {
                    lbl_connection.Text = "Connected to RaspiBot";
                };
                ws.Connect();
                ws.Send(test);
                //ws.Close();
                moved = test;
            }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            direction = "Standing";
            webSocket(direction);
        }

        private void btn_forward_Click(object sender, EventArgs e)
        {
            direction = "Forward";
        }

        private void btn_stand_Click(object sender, EventArgs e)
        {
            direction = "Standing";
        }

        private void btn_left_Click(object sender, EventArgs e)
        {
            direction = "Left";
        }

        private void btn_right_Click(object sender, EventArgs e)
        {
            direction = "Right";
        }

        private void btn_backwards_Click(object sender, EventArgs e)
        {
            direction = "Backwards";
            
        }

        private void btn_auto_Click(object sender, EventArgs e)
        {
            direction = "Auto";
        }
    }
}

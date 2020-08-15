namespace RaspiBot
{
    partial class Form1
    {
        /// <summary>
        /// Erforderliche Designervariable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Verwendete Ressourcen bereinigen.
        /// </summary>
        /// <param name="disposing">True, wenn verwaltete Ressourcen gelöscht werden sollen; andernfalls False.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Vom Windows Form-Designer generierter Code

        /// <summary>
        /// Erforderliche Methode für die Designerunterstützung.
        /// Der Inhalt der Methode darf nicht mit dem Code-Editor geändert werden.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.btn_forward = new System.Windows.Forms.Button();
            this.btn_right = new System.Windows.Forms.Button();
            this.btn_left = new System.Windows.Forms.Button();
            this.btn_backwards = new System.Windows.Forms.Button();
            this.btn_stand = new System.Windows.Forms.Button();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.lbl_connection = new System.Windows.Forms.Label();
            this.btn_arrow = new System.Windows.Forms.Button();
            this.btn_camera = new System.Windows.Forms.Button();
            this.btn_auto = new System.Windows.Forms.Button();
            this.grBox_control = new System.Windows.Forms.GroupBox();
            this.grBox_control.SuspendLayout();
            this.SuspendLayout();
            // 
            // btn_forward
            // 
            this.btn_forward.Location = new System.Drawing.Point(120, 54);
            this.btn_forward.Name = "btn_forward";
            this.btn_forward.Size = new System.Drawing.Size(75, 23);
            this.btn_forward.TabIndex = 0;
            this.btn_forward.Text = "Forward";
            this.btn_forward.UseVisualStyleBackColor = true;
            this.btn_forward.Click += new System.EventHandler(this.btn_forward_Click);
            // 
            // btn_right
            // 
            this.btn_right.Location = new System.Drawing.Point(201, 83);
            this.btn_right.Name = "btn_right";
            this.btn_right.Size = new System.Drawing.Size(75, 23);
            this.btn_right.TabIndex = 1;
            this.btn_right.Text = "Right";
            this.btn_right.UseVisualStyleBackColor = true;
            this.btn_right.Click += new System.EventHandler(this.btn_right_Click);
            // 
            // btn_left
            // 
            this.btn_left.Location = new System.Drawing.Point(39, 83);
            this.btn_left.Name = "btn_left";
            this.btn_left.Size = new System.Drawing.Size(75, 23);
            this.btn_left.TabIndex = 2;
            this.btn_left.Text = "Left";
            this.btn_left.UseVisualStyleBackColor = true;
            this.btn_left.Click += new System.EventHandler(this.btn_left_Click);
            // 
            // btn_backwards
            // 
            this.btn_backwards.Location = new System.Drawing.Point(120, 112);
            this.btn_backwards.Name = "btn_backwards";
            this.btn_backwards.Size = new System.Drawing.Size(75, 23);
            this.btn_backwards.TabIndex = 3;
            this.btn_backwards.Text = "Backwards";
            this.btn_backwards.UseVisualStyleBackColor = true;
            this.btn_backwards.Click += new System.EventHandler(this.btn_backwards_Click);
            // 
            // btn_stand
            // 
            this.btn_stand.Location = new System.Drawing.Point(120, 83);
            this.btn_stand.Name = "btn_stand";
            this.btn_stand.Size = new System.Drawing.Size(75, 23);
            this.btn_stand.TabIndex = 4;
            this.btn_stand.Text = "Stand";
            this.btn_stand.UseVisualStyleBackColor = true;
            this.btn_stand.Click += new System.EventHandler(this.btn_stand_Click);
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 50;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // lbl_connection
            // 
            this.lbl_connection.AutoSize = true;
            this.lbl_connection.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lbl_connection.ForeColor = System.Drawing.Color.Red;
            this.lbl_connection.Location = new System.Drawing.Point(86, 28);
            this.lbl_connection.Name = "lbl_connection";
            this.lbl_connection.Size = new System.Drawing.Size(114, 20);
            this.lbl_connection.TabIndex = 5;
            this.lbl_connection.Text = "No Connection";
            // 
            // btn_arrow
            // 
            this.btn_arrow.Location = new System.Drawing.Point(21, 217);
            this.btn_arrow.Name = "btn_arrow";
            this.btn_arrow.Size = new System.Drawing.Size(93, 23);
            this.btn_arrow.TabIndex = 6;
            this.btn_arrow.Text = "Arrow control";
            this.btn_arrow.UseVisualStyleBackColor = true;
            this.btn_arrow.Click += new System.EventHandler(this.btn_arrow_Click);
            this.btn_arrow.KeyDown += new System.Windows.Forms.KeyEventHandler(this.btn_arrow_KeyDown);
            // 
            // btn_camera
            // 
            this.btn_camera.Location = new System.Drawing.Point(120, 217);
            this.btn_camera.Name = "btn_camera";
            this.btn_camera.Size = new System.Drawing.Size(100, 23);
            this.btn_camera.TabIndex = 7;
            this.btn_camera.Text = "Enable Camera";
            this.btn_camera.UseVisualStyleBackColor = true;
            this.btn_camera.Click += new System.EventHandler(this.btn_camera_Click);
            // 
            // btn_auto
            // 
            this.btn_auto.Location = new System.Drawing.Point(226, 217);
            this.btn_auto.Name = "btn_auto";
            this.btn_auto.Size = new System.Drawing.Size(83, 23);
            this.btn_auto.TabIndex = 8;
            this.btn_auto.Text = "Enable Auto";
            this.btn_auto.UseVisualStyleBackColor = true;
            this.btn_auto.Click += new System.EventHandler(this.btn_auto_Click);
            // 
            // grBox_control
            // 
            this.grBox_control.Controls.Add(this.btn_auto);
            this.grBox_control.Controls.Add(this.btn_camera);
            this.grBox_control.Controls.Add(this.btn_arrow);
            this.grBox_control.Controls.Add(this.btn_stand);
            this.grBox_control.Controls.Add(this.btn_backwards);
            this.grBox_control.Controls.Add(this.btn_left);
            this.grBox_control.Controls.Add(this.btn_right);
            this.grBox_control.Controls.Add(this.btn_forward);
            this.grBox_control.Location = new System.Drawing.Point(13, 78);
            this.grBox_control.Name = "grBox_control";
            this.grBox_control.Size = new System.Drawing.Size(322, 257);
            this.grBox_control.TabIndex = 9;
            this.grBox_control.TabStop = false;
            this.grBox_control.Text = "Control";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.AutoSize = true;
            this.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
            this.ClientSize = new System.Drawing.Size(344, 345);
            this.Controls.Add(this.grBox_control);
            this.Controls.Add(this.lbl_connection);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form1";
            this.Text = "Form1";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.grBox_control.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btn_forward;
        private System.Windows.Forms.Button btn_right;
        private System.Windows.Forms.Button btn_left;
        private System.Windows.Forms.Button btn_backwards;
        private System.Windows.Forms.Button btn_stand;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Label lbl_connection;
        private System.Windows.Forms.Button btn_arrow;
        private System.Windows.Forms.Button btn_camera;
        private System.Windows.Forms.Button btn_auto;
        private System.Windows.Forms.GroupBox grBox_control;
    }
}


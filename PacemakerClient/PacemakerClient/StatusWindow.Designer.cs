﻿namespace PacemakerClient
{
    partial class StatusWindow
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.StatusLabel = new System.Windows.Forms.Label();
            this.uNameLabel = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // StatusLabel
            // 
            this.StatusLabel.AutoSize = true;
            this.StatusLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.StatusLabel.Location = new System.Drawing.Point(12, 29);
            this.StatusLabel.Name = "StatusLabel";
            this.StatusLabel.Size = new System.Drawing.Size(133, 20);
            this.StatusLabel.TabIndex = 0;
            this.StatusLabel.Text = "Telemetry Status:";
            // 
            // uNameLabel
            // 
            this.uNameLabel.AutoSize = true;
            this.uNameLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.uNameLabel.Location = new System.Drawing.Point(12, 9);
            this.uNameLabel.Name = "uNameLabel";
            this.uNameLabel.Size = new System.Drawing.Size(104, 20);
            this.uNameLabel.TabIndex = 1;
            this.uNameLabel.Text = "Current User:";
            // 
            // StatusWindow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(486, 286);
            this.Controls.Add(this.uNameLabel);
            this.Controls.Add(this.StatusLabel);
            this.Name = "StatusWindow";
            this.Text = "Pacemaker Client:";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label StatusLabel;
        private System.Windows.Forms.Label uNameLabel;
    }
}
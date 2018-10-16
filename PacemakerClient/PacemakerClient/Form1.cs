using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace PacemakerClient
{
    public partial class Login : Form
    {
        public Login()
        {
            InitializeComponent();
            //Open the data file and check the records I guess
            //Not sure if it should be one data file per patient and a big log for the rest or what?
        }

        private void registerlabel_Click(object sender, EventArgs e)
        {
            //Open up a new window to ask for username, password
        }

        private void LoginButton_Click(object sender, EventArgs e)
        {
            //Check if inputs are empty
            //Then check if inputs are in the database already
            //Then do the whole login thing
        }
    }
}

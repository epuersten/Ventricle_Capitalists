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
    public partial class Signup : Form
    {
        public Signup()
        {
            InitializeComponent();
        }

        /* Replace DataHandler with whatever object is used to access the data file
        public Signup(DataHandler handler)
        {
            InitializeComponent();
        }
        */

        private void SubmitButton_Click(object sender, EventArgs e)
        {
            //Probably validate the username doesnt exist in the data file
            //Then validate the passwords are the same
            //Then create the new entry in the data file, close, and go back to the previous screen
        }
    }
}

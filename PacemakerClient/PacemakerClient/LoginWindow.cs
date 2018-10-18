﻿using System;
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
            //Open the data file for the records here. 
            //I think it might be good to create an object for this, open the file, and then pass it to the other windows as we go along
            //Build it how you want though, and I'll work around it ^^

            //DataHandler data = new DataHandler();

            //Probably going to be a big table that holds patient names on the first column and all the other information on ones further down.
        }

        private void registerlabel_Click(object sender, EventArgs e)
        {
            //Open up a new window to ask for username, password
            //This will open SignupWindow and pass the data handler object to it
            Signup signup = new Signup();
            //We show it as a dialog so that the user can't interact with this window until it's filled out
            signup.ShowDialog();
        }

        private void LoginButton_Click(object sender, EventArgs e)
        {
            //Get username and password strings
            String username = usernameBox.Text;
            String password = passwordBox.Text;
            //Check if inputs are empty
            if(usernameBox.Text.Length == 0 || passwordBox.Text.Length == 0)
            {
                //Show an error dialog

                //Clear the fields
                usernameBox.Text = "";
                passwordBox.Text = "";
            }
            //Then check if inputs are in the database already (After the data file has been opened)
            //Try and see if the user is valid first, then the password. Maybe have a table and use the user as a key, password as one of the values in it?
            
            //If they are both valid, open up the controller/telemetry window and pass it the username.
            //Then we can use the username there as a key to access the rest of the user data inside the DataHandler.

        }

    }
}
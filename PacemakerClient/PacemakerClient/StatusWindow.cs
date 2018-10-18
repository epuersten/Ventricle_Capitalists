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
    public partial class StatusWindow : Form
    {
        //States for the connected pacemaker telemetry.
        private enum TELEMETRY_STATES {CONNECTED, DISCONNECTED};
        //Pacing states for the connected pacemaker
        private enum PACE_STATES { AOO, VOO};

        //Add a second parameter for the data object later
        public StatusWindow(String username)
        {
            InitializeComponent();
            uNameLabel.Text = uNameLabel.Text + username; //Shows the current user that is logged on
        }
    }
}

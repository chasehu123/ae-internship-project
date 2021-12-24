using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AE_Demo
{
    public partial class Sub : Form
    {
        public Sub()
        {
            InitializeComponent();
        }

        private void Sub_Load(object sender, EventArgs e)
        {
            axSceneControl1.LoadSxFile(@"../Data/scene/scene.sxd");
        }

        private void axSceneControl1_OnMouseDown(object sender, ESRI.ArcGIS.Controls.ISceneControlEvents_OnMouseDownEvent e)
        {

        }
    }
}

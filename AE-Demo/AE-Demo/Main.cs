using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using ESRI.ArcGIS.Geoprocessor;
using ESRI.ArcGIS.AnalysisTools;

namespace AE_Demo
{
    public partial class MainPage : Form
    {
        public MainPage()
        {
            InitializeComponent();
        }

        private void generateBufferToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Geoprocessor GP = new Geoprocessor();
            GP.OverwriteOutput = true;
            ESRI.ArcGIS.AnalysisTools.Buffer buffer = new ESRI.ArcGIS.AnalysisTools.Buffer();
            buffer.in_features = @"..\Data\line.shp";
            buffer.out_feature_class = @"..\Data\line_buf.shp";
            buffer.buffer_distance_or_field = "3 Kilometers";
            MessageBox.Show("点击确定开始缓冲区分析!");
            GP.Execute(buffer, null);
            MessageBox.Show("处理成功!缓冲区大小为3公里!");
            string path = @"..\Data";
            string line_buf = "line_buf.shp";
            axMapControl1.AddShapeFile(path, line_buf);
        }

        private void MainPage_Load(object sender, EventArgs e)
        {
            string path = @"..\Data";
            string area = "area.shp";
            string line = "line.shp";
            axMapControl1.AddShapeFile(path, area);
            axMapControl1.AddShapeFile(path, line);
        }

        private void loadFileToolStripMenuItem_Click(object sender, EventArgs e)
        {
            axMapControl1.LoadMxFile(@"..\Data\mask\mask.mxd");
        }

        private void processToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MessageBox.Show("点击开始处理!");
            //Sub.ActiveForm.ShowDialog();
            //Application.Run(new Sub());
            Sub SubPage = new Sub();
            SubPage.ShowDialog();
            //MessageBox.Show("处理结束!");
        }
    }
}

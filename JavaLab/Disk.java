package disk;

import java.awt.*;
import java.applet.*;

/*<applet code="Disk.class" width=500 height=500 />*/



public class Disk extends Applet{

	Color color[] = {Color.cyan , Color.blue, Color.orange,Color.pink,Color.yellow,Color.red};
	public void init() {
		setBackground(Color.green);
	}

	public void paint(Graphics g) {
		int colorlen = color.length;
		g.drawString("Rotating Disk Color", 100, 20);

		int index;
		while(true) {
			for (int i=0;i<colorlen;i++) {
				index = Math.abs(colorlen - i);

				if (index > 5)
					index = 0;
					g.setColor(color[index]);
					g.fillArc(20, 20, 150, 150, 0, 60);
					++index;
				if (index > 5)
						index = 0;
						g.setColor(color[index]);
						g.fillArc(20, 20, 150, 150, 0, 60);
						++index;
				if (index > 5)
						index = 0;
						g.setColor(color[index]);
						g.fillArc(20, 20, 150, 150, 0, 60);
						++index;
				if (index > 5)
						index = 0;
						g.setColor(color[index]);
						g.fillArc(20, 20, 150, 150, 0, 60);
						++index;
				if (index > 5)
						index = 0;
						g.setColor(color[index]);
						g.fillArc(20, 20, 150, 150, 0, 60);
						++index;
				if (index > 5)
						index = 0;
						g.setColor(color[index]);
						g.fillArc(20, 20, 150, 150, 0, 60);
						++index;

				try {
					Thread.sleep(2000);
				}
				catch(Exception e) {}
			}
		}
	}

}

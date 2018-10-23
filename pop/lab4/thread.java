import java.util.*;

class multi implements Runnable
{
	public  void run()
	{
		synchronized(this)
		{
            for(int i = 0; i < 3; i++) {
                System.out.println(i);
            }
		}
	}
}

class thread
{
	public static void main(String[] args)
	{
		multi m1 = new multi();
		multi m2 = new multi();

		Thread t1 = new Thread(m1);
		Thread t2 = new Thread(m2);

		t1.start();
		t2.start();
	}
}
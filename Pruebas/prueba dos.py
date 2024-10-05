using System.Linq;

public class Dinglemouse
{
  public static int[] ShakeTree(string[] tree)
  {
    //Your code here
    return new int[tree[0].Length].Select(v => 0).ToArray();
  }
}

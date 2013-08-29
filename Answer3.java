import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;


public class Answer3 
{
	ArrayList<Case> cases;
	
	public static void main(String[] args) throws IOException
	{
		BufferedReader reader = null;
		String input;
		
		Answer3 current = new Answer3();
		
		try
		{
			reader = new BufferedReader(new FileReader(args[0]));
			
			// The first line is the number of games we are given as input
			input = reader.readLine();
			int numCases = Integer.parseInt(input);
			
			// Run through the file reading all of the games we've been told to read
			int currentCase = 0;
			String line1;
			String line2;
			while(currentCase < numCases)
			{
				line1 = reader.readLine();
				line2 = reader.readLine();
				current.addCase(line1, line2);
				currentCase++;
			}
		}
		catch(IOException ex)
		{
			//Handle any IO exceptions.
			ex.printStackTrace();
		}
		finally
		{
			//Close the file.
			reader.close();
		}
		
		current.run();
	}
	
	private Answer3()
	{
		cases = new ArrayList<Case>();
	}
	
	private void addCase(String line1, String line2)
	{
		//line 1 is X Y, where X is number of cannon and Y is number of firers
		//who will be assassinated.
		
		String[] lineParsed = new String[2];
		lineParsed = line1.split(" ");
		
		int numCannons = Integer.parseInt(lineParsed[0]);
		int numToBeAssassinated = Integer.parseInt(lineParsed[1]);
		
		int[] toBeAssassinated = new int[numToBeAssassinated];
		lineParsed = new String[numToBeAssassinated];
		
		lineParsed = line2.split(" ");
		
		for(int i = 0; i < numToBeAssassinated; i++)
		{
			toBeAssassinated[i] = Integer.parseInt(lineParsed[i]);
		}
		
		Case newCase = new Case(numCannons, numToBeAssassinated, toBeAssassinated);
		
		cases.add(newCase);
	}
	
	private void run()
	{
		int caseCount = 1;
		for(Case currentCase : cases)
		{
			currentCase.run(caseCount++);
		}
	}
	
	
	
	
	private class Case
	{
		private ArrayList<ArrayList<Integer>> permutations;	// A list of the orders in which
		// the firers could be killed.
		int[] toBeAssassinated;
		int numCannons;
		int numToBeAssassinated;
		boolean[] alive;
		int maxShots;
		
		public Case(int numCannons, int numToBeAssassinated, int[] toBeAssassinated)
		{
			this.numCannons = numCannons;	//num cannons
			this.numToBeAssassinated = numToBeAssassinated; //num people to be assassinated
			
			this.toBeAssassinated = new int[numToBeAssassinated];
			for(int i = 0; i < this.numToBeAssassinated; i++)
			{
				this.toBeAssassinated[i] = toBeAssassinated[i];
			}
			
			permutations = new ArrayList<ArrayList<Integer>>();
			
			alive = new boolean[this.numCannons+1];
		}
		
		private void run(int caseCount)
		{
			createPermutations();	//create list of permutations
			
			int numberOfShots = 0;
			maxShots = 0;
			
			for(ArrayList<Integer> permutation : permutations)
			{
				// Run a single permutation and see how many shots are fired for this:
				numberOfShots = getMaxNumberOfShotsForPermutation(permutation);
				if(numberOfShots > maxShots)
				{
					maxShots = numberOfShots;
				}
			}
			
			//print maxShots here!!!!!!!
			System.out.format("Case%d: %d", caseCount, maxShots);
			System.out.print('\n');
		}
		
		
		private int getMaxNumberOfShotsForPermutation(ArrayList<Integer> permutation)
		{
			for(int i = 1; i < numCannons+1; i++){ alive[i] = true;}	//all gunners alive at start
			
			int numberOfShots = 0;
			
			for(int gunnerToKill : permutation)
			{
				alive[gunnerToKill] = false;
				numberOfShots += shotsToLeft(gunnerToKill);
				numberOfShots += shotsToRight(gunnerToKill);
			}
			
			return numberOfShots;
		}
		
		private int shotsToLeft(int gunnerJustKilled)
		{
			int current = gunnerJustKilled - 1;
			int numberOfShots = 0;
			
			while(current >= 1 && (alive[current] == true))
			{
				numberOfShots++;
				current--;	//move left
			}
			
			return numberOfShots;
		}
		
		private int shotsToRight(int gunnerJustKilled)
		{
			int current = gunnerJustKilled + 1;
			int numberOfShots = 0;
			
			while(current <= numCannons && (alive[current] == true))
			{
				numberOfShots++;
				current++;	//move right
			}		
			
			return numberOfShots;
		}
		
		
		//run the simulation
		private void createPermutations()
		{
			//do
			ArrayList<Integer> current = new ArrayList<Integer>();
			boolean[] used = new boolean[numToBeAssassinated];
			int length = numToBeAssassinated;
			int level = 0;
			
			permuteArray(toBeAssassinated, current, used, length, level);
		}
		
		private void permuteArray(	int[] ref,
									ArrayList<Integer> current,
									boolean[] used,
									int length,
									int level)
		{	
			if(level == length)
			{
				ArrayList<Integer> copyOfCurrent = new ArrayList<Integer>();
				copyArrayListOfInts(copyOfCurrent, current);
				permutations.add(copyOfCurrent);
				return;
			}
			
			for(int i = 0; i < ref.length; ++i)
			{
				if(used[i])
				{
					continue;
				}
				
				current.add(ref[i]);
				used[i] = true;
				permuteArray(ref, current, used, length, level+1);
				used[i] = false;
				current.remove(current.size()-1);	//remove last element
			}
		}

		private void copyArrayListOfInts(ArrayList<Integer> copyOfCurrent, ArrayList<Integer> current)
		{
			copyOfCurrent.ensureCapacity(current.size());
			for(Integer currInt : current)
			{
				copyOfCurrent.add(currInt);
			}
		}
	}
}

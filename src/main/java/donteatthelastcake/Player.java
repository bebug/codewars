package donteatthelastcake;

public class Player {
    public Player(int cakes) {
    }
    // Decide who move first - player or opponent (true if player)
    public boolean firstMove(int cakes) {
        return cakes != 1 && cakes != 2 && (cakes-6)%4 != 0;
    }

    // Decide your next move
    public int move(int cakes, int last) {
        if (cakes == 1 || cakes == 2)
            return last == 1 ? 2: 1;
        else if (cakes == 3)
            return last == 1 ? 2 : 1;
        else if (cakes % 4 == 0)
            return last == 3 ? 2: 3;
        else if ((cakes-1) % 4 == 0)
            return last != 3 ? 3 : 1;
        else if ((cakes+1) % 4 == 0)
            return last != 1 ? 1: 2;
        else return last == 1 ? 2: 1;
    }
}

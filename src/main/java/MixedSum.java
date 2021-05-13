import java.util.List;

public class MixedSum {

    /*
     * Assume input will be only of Integer o String type
     */
    public int sum(List<?> mixed) {
        return mixed.stream().mapToInt(x -> {
            if (x instanceof String) return Integer.parseInt((String)x);
            return (Integer) x;
        }).sum();
    }
}
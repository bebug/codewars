package statisticsforanathletic;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class Stat {

    public static String stat(String strg) {
        if (strg == null || strg.isEmpty()) {
            return "";
        }

        List<Long> durations = parseDurations(strg);
        durations.sort(Long::compareTo);

        Long range = durations.get(durations.size() - 1) - durations.get(0);
        Long median = durations.size() % 2 == 0 ? (durations.get(durations.size()/2) + durations.get(durations.size()/2 -1))/2 : durations.get(durations.size()/2);
        Long mean = durations.stream().reduce(Long::sum).orElse(0L)/durations.size();

        return printOutput(range, median, mean);
    }

    private static String printOutput(Long range, Long median, Long mean) {
        return "Range: " + printDurations(range) + " Average: " + printDurations(mean) + " Median: " + printDurations(median);
    }

    private static String printDurations(Long time) {
        Long seconds = time%60;
        Long minutes = time/60%60;
        Long hours = time/3600;
        return String.format("%02d|%02d|%02d", hours, minutes, seconds);
    }

    public static List<Long> parseDurations(String strg) {
        if (strg.isEmpty())
            return Collections.emptyList();
        return Arrays.stream(strg.split(",")).map(s -> {
            String[] parts = s.trim().split("\\|");
            return Long.parseLong(parts[0]) * 3600 + Long.parseLong(parts[1]) * 60 + Long.parseLong(parts[2]);
        }).collect(Collectors.toList());
    }

}

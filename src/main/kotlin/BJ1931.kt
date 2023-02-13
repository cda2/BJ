object BJ1931 {
    data class Meeting(val start: Int, val end: Int) : Comparable<Meeting> {
        fun canContinue(meeting: Meeting): Boolean {
            return end <= meeting.start
        }

        fun canContain(meeting: Meeting): Boolean {
            return start <= meeting.start && end >= meeting.end
        }

        override fun compareTo(other: Meeting): Int {
            return when (end) {
                other.end -> start - other.start
                else -> end - other.end
            }
        }
    }

    fun solution(list: List<Meeting>): Int {
        val sortedMeetings = list.sorted()
        var count = 0

        var lastMeeting = Meeting(0, 0)
        for (meeting in sortedMeetings) {
            if (lastMeeting.canContain(meeting)) {
                lastMeeting = meeting
            }
            if (lastMeeting.canContinue(meeting)) {
                lastMeeting = meeting
                count++
            }
        }

        return count
    }

    fun solve() {
        val n = readln().toInt()
        val meetings = mutableListOf<Meeting>()
        repeat(n) {
            val (start, end) = readln()
                    .split(" ")
                    .map { it.toInt() }
            meetings.add(Meeting(start, end))
        }
        println(solution(meetings))
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}

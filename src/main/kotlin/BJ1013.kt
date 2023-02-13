class BJ1013(private val pattern: String = "(100+1+ | 01)+") {

    fun solution(str: String): String {
        return pattern.replace(" ", "").toRegex().matches(str).let { if (it) "YES" else "NO" }
    }

    fun solve() {
        val n = readln().toInt()
        repeat(n) { println(solution(readln())) }
    }

    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            BJ1013().solve()
        }
    }
}

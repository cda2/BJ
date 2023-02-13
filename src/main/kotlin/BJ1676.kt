object BJ1676 {
    fun solution(n: Int): Int {
        var count = 0
        var i = 5
        while (i <= n) {
            count += n / i
            i *= 5
        }
        return count
    }

    fun solve() {
        val n = readln().toInt()
        println(solution(n))
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}

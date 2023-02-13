object BJ11399 {
    fun solution(list: List<Int>): Int {
        // sort list, and make list prefix array, and sum it.
        return list
                .sorted()
                .scan(0) { acc, i -> acc + i }
                .scan(0) { acc, i -> acc + i }
                .last()
    }

    fun solve() {
        val n = readln().toInt()
        val list = readln()
                .split(" ")
                .map { it.toInt() }
        println(solution(list))
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}

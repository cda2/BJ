object BJ18870 {
    fun solution(list: List<Int>): List<Int> {
        val indexMap: MutableMap<Int, Int> = list
                .distinct()
                .sorted()
                .mapIndexed { index, i -> i to index }
                .toMap()
                .toMutableMap()
        return list.map { indexMap[it]!! }
    }

    fun solve() {
        val n = readln().toInt()
        val list = readln()
                .split(" ")
                .map { it.toInt() }
        println(solution(list).joinToString(" "))
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}

object BJ9095 {
    val arr: MutableList<Int> = mutableListOf(1, 2, 4)

    fun solution(n: Int): Int {
        if (n <= arr.size) {
            return arr[n - 1]
        }

        for (i in arr.size until n) {
            arr.add(arr[i - 1] + arr[i - 2] + arr[i - 3])
        }
        return arr[n - 1]
    }

    fun solve() {
        val n = readln().toInt()
        repeat(n) {
            val num = readln().toInt()
            println(solution(num))
        }
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}

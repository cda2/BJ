object BJ1083 {

    fun solution(list: List<Int>, s: Int): List<Int> {
        if (list.size <= 1) return list

        val arr = list.toMutableList()
        var count: Int = s

        for (curIndex in 0 until arr.size - 1) {
            if (count == 0) break
            val maximumReach = minOf(curIndex + count, arr.size - 1)
            var maxIndex = curIndex
            for (candidateIndex in curIndex + 1..maximumReach) {
                if (arr[candidateIndex] > arr[maxIndex]) {
                    maxIndex = candidateIndex
                }
            }
            if (maxIndex != curIndex) {
                val maxValue = arr.removeAt(maxIndex)
                arr.add(curIndex, maxValue)
                count -= maxIndex - curIndex
            } else {
                continue
            }
        }
        return arr
    }

    fun solve() {
        val n = readln().toInt()
        val arr = readln()
                .split(" ")
                .map { it.toInt() }
                .toMutableList()
        val s = readln().toInt()
        println(solution(arr, s).joinToString(" "))
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}

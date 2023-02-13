object BJ1780 {
    fun solution(bigPaper: List<List<Int>>): Triple<Int, Int, Int> {
        data class Paper(val y: Int, val x: Int, val size: Int) {
            val rowIndices: IntRange = y until y + size
            val colIndices: IntRange = x until x + size
            val getValue = bigPaper[y][x]
            fun smallPart(): List<Paper> {
                val list = mutableListOf<Paper>()
                val miniSize = size / 3
                for (i in 0..2) {
                    for (j in 0..2) {
                        list.add(Paper(y + miniSize * i, x + miniSize * j, miniSize))
                    }
                }
                return list
            }
        }

        data class Status(var minus: Int = 0, var zero: Int = 0, var plus: Int = 0) {
            operator fun plusAssign(other: Status) {
                minus += other.minus
                zero += other.zero
                plus += other.plus
            }
        }

        fun recursiveCheck(partPaper: Paper): Status {
            val type = partPaper.getValue
            for (row in partPaper.rowIndices) {
                for (col in partPaper.colIndices) {
                    val value = bigPaper[row][col]
                    if (value != type) {
                        val answer = Status(0, 0, 0)
                        partPaper
                                .smallPart()
                                .map { recursiveCheck(it) }
                                .map { answer += it }
                        return answer
                    }
                }
            }
            return when(type) {
                -1 -> Status(1, 0, 0)
                0 -> Status(0, 1, 0)
                1 -> Status(0, 0, 1)
                else -> throw Exception("Error")
            }
        }

        return recursiveCheck(Paper(0, 0, bigPaper.size)).let { Triple(it.minus, it.zero, it.plus) }
    }

    fun solve() {
        val br = System.`in`.bufferedReader()
        val n = br
                .readLine()
                .toInt()
        val bigPaper = mutableListOf<List<Int>>()
        repeat(n) {
            bigPaper.add(
                br
                        .readLine()
                        .split(" ")
                        .map { it.toInt() }
                        .toList()
            )
        }
        solution(bigPaper).let { println(it.first); println(it.second); println(it.third) }
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}

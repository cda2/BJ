object BJ1992 {
    data class Status(val y: Int, val x: Int, val size: Int)

    fun solution(dots: List<List<Int>>): String {

        fun compression(status: Status): String {
            val intType = dots[status.y][status.x]
            var isAllSame = true
            for (yy in status.y until status.y + status.size) {
                for (xx in status.x until status.x + status.size) {
                    val value = dots[yy][xx]
                    if (value != intType) {
                        isAllSame = false
                        break
                    }
                }
            }
            return if (isAllSame) {
                intType.toString()
            } else {
                val halfSize = status.size / 2
                val stringBuffer = StringBuffer("(")
                for (ii in 0..1) {
                    for (jj in 0..1) {
                        stringBuffer.append(
                            compression(
                                Status(status.y + halfSize * ii, status.x + halfSize * jj, halfSize)
                            )
                        )
                    }
                }
                stringBuffer.append(")")
                return stringBuffer.toString()
            }
        }

        return compression(Status(0, 0, dots.size))
    }

    fun solve() {
        val n: Int = readln().toInt()
        val dots = mutableListOf<List<Int>>()
        repeat(n) {
            val arr = readln()
                    .trim()
                    .toList()
                    .map { it.digitToInt() }
            dots.add(arr)
        }

        println(solution(dots))
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}

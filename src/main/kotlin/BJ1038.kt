import kotlin.math.pow

object BJ1038 {
    val answerList = getFullList()

    fun getFullList(): List<Long> {
        val setListMap = hashMapOf<Int, ArrayList<HashSet<Long>>>()
        for (i in 0..9) {
            if (i == 0) {
                setListMap[i] = (0..9).map { hashSetOf(it.toLong()) }.toCollection(arrayListOf())
            } else {
                val arr = Array(10) { hashSetOf<Long>() }.toCollection(arrayListOf())
                for (j in i..9) {
                    for (k in 0 until j) {
                        arr[j].addAll(
                            setListMap[i - 1]!![k].map {
                                val multiplier = getMultiplier(it)
                                val up = ((10).toDouble().pow(multiplier) * j).toLong()
                                val i1 = up + it
                                i1
                            })
                    }
                }
                setListMap[i] = arr
            }
        }

        return setListMap.values.flatten().filter { it.isNotEmpty() }.flatten().sorted()
    }

    fun solution(n: Int): Long {
        return if (n >= this.answerList.size) -1 else this.answerList[n]
    }

    fun getMultiplier(num: Long): Int {
        return num.toString().length
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

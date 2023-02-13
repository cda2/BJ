import java.util.*

object BJ7662 {
    class MinMaxHeap<T : Comparable<T>> {
        private val visited = mutableMapOf<T, Int>().withDefault { 0 }
        private val minHeap = PriorityQueue<T>()
        private val maxHeap = PriorityQueue<T>(Comparator.reverseOrder())
        fun insert(value: T) {
            minHeap.add(value)
            maxHeap.add(value)
            visited[value] = visited.getValue(value) + 1
        }

        fun isEmpty(): Boolean = minHeap.isEmpty() || maxHeap.isEmpty()
        fun minValue(): T? = minHeap.peek()
        fun maxValue(): T? = maxHeap.peek()
        fun popMin(): T? {
            syncInternal(minHeap)
            return remove(minHeap)
        }

        fun popMax(): T? {
            syncInternal(maxHeap)
            return remove(maxHeap)
        }

        fun sync() {
            syncInternal(minHeap)
            syncInternal(maxHeap)
        }

        private fun syncInternal(heap: PriorityQueue<T>) {
            while (heap.isNotEmpty() && visited[heap.peek()]?.let { it <= 0 } == true) {
                heap.poll()
            }
        }

        private fun remove(heap: PriorityQueue<T>): T? {
            return if (heap.isNotEmpty()) {
                val v = heap.poll()
                visited[v] = visited.getValue(v) - 1
                v
            } else {
                null
            }
        }
    }

    fun solution(list: List<String>): String {
        val minMaxHeap = MinMaxHeap<Int>()

        for (line in list) {
            val (command, value) = line.split(" ")
            when (command) {
                "I" -> {
                    val v = value.toInt()
                    minMaxHeap.insert(v)
                }

                "D" -> {
                    if (minMaxHeap.minValue() == null) {
                        continue
                    }

                    if (value == "1") {
                        minMaxHeap.popMax()
                    } else {
                        minMaxHeap.popMin()
                    }
                }
            }
        }
        minMaxHeap.sync()

        return if (minMaxHeap.isEmpty()) {
            "EMPTY"
        } else {
            "${minMaxHeap.maxValue()} ${minMaxHeap.minValue()}"
        }
    }

    @JvmStatic
    fun main(args: Array<String>) {
        val bufferedReader = System.`in`.bufferedReader()
        val bufferedWriter = System.out.bufferedWriter()
        val t = bufferedReader
                .readLine()
                .toInt()
        repeat(t) {
            val k = bufferedReader
                    .readLine()
                    .toInt()
            val list = mutableListOf<String>()
            repeat(k) {
                list.add(bufferedReader.readLine())
            }
            val result = solution(list)
            bufferedWriter.write("$result\n")
        }
        bufferedWriter.flush()
    }
}

<template>
  <status-chart :chartdata="chartdata" :options="chartOptions" />
</template>

<script>
import statusChart from './statusChart'
export default {
  components: {
    statusChart
  },
  data() {
    return {
      chartdata: {
        labels: ['자본금', '총자산 합계', '총부채'],
        datasets: [
          {
            backgroundColor: ['#41B883', '#E46651', '#00D8FF'],
            data: [4000, 2000, 8500]
          }
        ]
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false
      }
    }
  }
}
</script>

<template>
  <inv-chart :chartdata="chartdata" :options="chartOptions" />
</template>

<script>
import invChart from './invChart'
export default {
  components: {
    invChart
  },
  data() {
    return {
      chartdata: {
        labels: [
          'January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December'
        ],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '#f87979',
            data: [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 11]
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

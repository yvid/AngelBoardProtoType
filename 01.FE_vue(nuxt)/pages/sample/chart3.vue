<template>
  <bubble-chart :chartdata="chartdata" :options="chartOptions" />
</template>

<script>
import bubbleChart from './bubbleChart'
export default {
  components: {
    bubbleChart
  },
  data() {
    return {
      chartdata: {
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '#f87979',
            data: [
              {
                x: 20,
                y: 25,
                r: 5
              },
              {
                x: 40,
                y: 10,
                r: 10
              },
              {
                x: 30,
                y: 22,
                r: 30
              }
            ]
          },
          {
            label: 'Data Two',
            backgroundColor: '#7C8CF8',
            data: [
              {
                x: 10,
                y: 30,
                r: 15
              },
              {
                x: 20,
                y: 20,
                r: 10
              },
              {
                x: 15,
                y: 8,
                r: 30
              }
            ]
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

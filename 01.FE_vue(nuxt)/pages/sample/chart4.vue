<template>
  <radar-chart :chartdata="chartdata" :options="chartOptions" />
</template>

<script>
import radarChart from './radarChart'
export default {
  components: {
    radarChart
  },
  data() {
    return {
      chartdata: {
        labels: ['1억 이하', '1~5억', '5~10억', '10억 이상'],
        datasets: [
          {
            label: '투자희망금액',
            backgroundColor: 'rgba(179,181,198,0.33)',
            borderColor: 'rgba(179,181,198,1)',
            pointBackgroundColor: 'rgba(179,181,198,1)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#ffd',
            pointHoverBorderColor: 'rgba(179,181,198,1)',
            data: [10, 5, 5, 5]
          },
          {
            label: '연간매출 희망금액',
            backgroundColor: 'rgba(179,181,198,0.33)',
            borderColor: 'rgba(179,181,198,1)',
            pointBackgroundColor: 'rgba(179,181,198,1)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgba(179,181,198,1)',
            data: [5, 10, 5, 5]
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

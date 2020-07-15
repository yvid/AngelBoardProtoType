<template>
  <body>
    <v-row>
      <v-col v-for="(item, i) in humanList" :key="i" cols="3">
        <v-card class="mx-auto" max-width="344" outlined>
          <v-list-item three-line>
            <v-list-item-content>
              <div class="overline mb-2">
                설립일: {{ item.foundedDate | unixTimeFilter }}
              </div>
              <div class="overline mb-1">{{ item.coNameEng }}</div>
              <v-list-item-title class="mb-3">{{
                item.coNameKor
              }}</v-list-item-title>
              <v-list-item-subtitle>{{ item.smallField }}</v-list-item-subtitle>
            </v-list-item-content>

            <img
              class="ma-2"
              onerror="this.src='/null_logo.png'"
              :src="item.coLogo"
              style="max-heght: 100px; max-width: 100px;"
            />
          </v-list-item>

          <v-card-text>
            <v-chip color="success" outlined small>{{
              item.tech | techFilter
            }}</v-chip>
            <v-chip class="ma-1" color="primary" outlined pill small>{{
              item.largeField | largeFieldFilter
            }}</v-chip>
            <v-chip color="orange" outlined pill small>{{
              item.serviceType | serviceTypeFilter
            }}</v-chip>
          </v-card-text>

          <v-card-actions>
            <v-btn
              text
              color="deep-purple accent-1"
              @click="
                $router.push({
                  path: `/human/humanView`,
                  query: { hSerial: item.hSerial }
                })
              "
            >
              More...
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </body>
</template>

<script>
import category from '~/pages/sample/category'

export default {
  filters: {
    unixTimeFilter(val) {
      const date = new Date(val + 1000)
        .toISOString()
        .slice(0, 19)
        .replace('T', ' ')
      return date.substring(0, 10)
    },
    techFilter(val) {
      const tech = category.tech

      let res = null
      for (const i in tech) {
        res = tech[i].value === val ? tech[i].text : res
      }

      return res
    },
    largeFieldFilter(val) {
      const largeField = category.largeField

      let res = null
      for (const i in largeField) {
        res = largeField[i].value === val ? largeField[i].text : res
      }

      return res
    },
    serviceTypeFilter(val) {
      const serviceType = category.serviceType
      let res = null
      for (const i in serviceType) {
        res = serviceType[i].value === val ? serviceType[i].text : res
      }

      return res
    },
    serviceStatusFilter(val) {
      const serviceStatus = category.serviceStatus
      let res = null
      for (const i in serviceStatus) {
        res = serviceStatus[i].value === val ? serviceStatus[i].text : res
      }

      return res
    }
  },
  data() {
    return {
      humanList: null
    }
  },
  created() {
    this.testArr()
  },
  methods: {
    testArr() {
      this.$axios
        .post('/api/human/list')
        .then((res) => {
          this.humanList = res.data[0]
        })
        .catch((err) => {
          throw err
        })
    },
    imageErrHandler(e) {
      console.error(e)
    }
  }
}
</script>

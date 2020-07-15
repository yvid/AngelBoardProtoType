<template>
  <v-container fluid>
    <v-data-iterator
      :items="items"
      :search="search"
      :sort-by="sortBy"
      :sort-desc="sortDesc"
      hide-default-footer
      no-data-text="투자 활동 현황 데이터가 없습니다."
      no-results-text="찾는 투자 현황 결과가 없습니다."
    >
      <template v-slot:header>
        <v-toolbar dark color="blue darken-3" class="mb-1">
          <v-text-field
            v-model="search"
            clearable
            flat
            solo-inverted
            hide-details
            prepend-inner-icon="search"
            label="Search"
          ></v-text-field>
        </v-toolbar>
      </template>

      <template v-slot:default="props">
        <div>
          <v-card v-if="dialog">
            <v-card-title>
              <span class="headline">
                <v-icon>mdi-chart-bubble</v-icon>
                엔젤보드 투자 연결 서비스 현황 세부정보
              </span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="selectedRow.aCoName"
                      label="투자사"
                      outlined
                      :readonly="!adminOn"
                      dense
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="selectedRow.hCoName"
                      label="투자 유치사"
                      outlined
                      :readonly="!adminOn"
                      dense
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-select
                      v-model="selectedRow.invType"
                      :items="invReqType"
                      label="투자신청 유형"
                      outlined
                      readonly
                      dense
                    >
                    </v-select>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-select
                      v-model="selectedRow.invStep"
                      :items="invStep"
                      label="진행 단계"
                      outlined
                      :readonly="!adminOn"
                      dense
                    >
                    </v-select>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="selectedRow.chngDate"
                      label="진행 상태 변경일"
                      outlined
                      :readonly="!adminOn"
                      dense
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                v-if="adminOn"
                color="blue darken-1"
                text
                @click="selectedRowUpdate()"
                >저장</v-btn
              >
              <v-btn color="blue darken-1" text @click="dialog = !dialog"
                >닫기</v-btn
              >
            </v-card-actions>
          </v-card>
        </div>

        <v-data-table
          :headers="headers"
          :items="props.items"
          :items-per-page="10"
          item-key="name"
          class="elevation-1"
        >
          <template v-slot:item.invStep="{ item }">
            <v-chip label :color="getColor(item.invStep)" dark>{{
              item.invStep
            }}</v-chip>
          </template>

          <template v-slot:item.actions="{ item }">
            <v-icon
              v-if="adminOn"
              medium
              class="mr-2"
              @click="getSelectedRow(item)"
            >
              mdi-pencil
            </v-icon>
            <v-icon
              v-if="!adminOn"
              medium
              class="mr-2"
              @click="getSelectedRow(item)"
            >
              search
            </v-icon>
          </template>
        </v-data-table>
      </template>
    </v-data-iterator>
  </v-container>
</template>

<script>
import category from '~/pages/sample/category'

export default {
  data() {
    return {
      adminOn: false,
      headers: [
        { text: '투자기업', value: 'aCoName' },
        { text: '투자유치기업', value: 'hCoName' },
        { text: '현재 상태', value: 'invStep' },
        { text: '투자 유형', value: 'invType' },
        {
          text: '상태 변경일',
          align: 'start',
          value: 'chngDate'
        },
        { text: '신청일', value: 'reqDate' },
        { text: '상세 보기', value: 'actions', sortable: false }
      ],
      itemsPerPageArray: [4, 8, 12],
      search: '',
      filter: {},
      sortDesc: false,
      sortBy: 'iSerial',
      keys: [
        { key: 'aCoName', value: '투자사' },
        'aCoName',
        'hCoName',
        'invStep',
        'invType',
        'chngDate',
        'reqDate'
      ],
      dialog: false,
      selectedRow: {},
      items: [],
      invReqType: [],
      invStep: []
    }
  },
  computed: {
    filteredKeys() {
      return this.keys.filter((key) => key !== `Name`)
    }
  },
  created() {
    this.invReqType = category.invReqType
    this.invStep = category.invStep
  },
  mounted() {
    this.setAdmin()
  },
  methods: {
    selectedRowUpdate() {
      this.$axios
        .post('/api/inv/updater', JSON.stringify(this.selectedRow))
        .then((res) => {
          this.callbackSelectedRowUpdate(res.data.updateRes[0])
        })
        .catch((err) => console.error(err))
    },
    callbackSelectedRowUpdate(row) {
      this.selectedRow.chngDate = this.unixTimeFilter(row.chngDate)
      this.selectedRow.invStep = row.invStep

      for (const i in this.items) {
        if (this.items[i].iSerial === row.iSerial) {
          this.items[i].chngDate = this.selectedRow.chngDate
          this.items[i].invStep = this.invStepFilter(this.selectedRow.invStep)
        }
      }
    },
    unixTimeFilter(val) {
      const date = new Date(val + 1000)
        .toISOString()
        .slice(0, 19)
        .replace('T', ' ')
      return date
    },
    invReqTypeFilter(val) {
      const invReqType = category.invReqType

      let res = null
      if (val.substring(0, 1) === 'a' || val.substring(0, 1) === 'h') {
        for (const i in invReqType) {
          res = invReqType[i].value === val ? invReqType[i].text : res
        }
        return res
      }

      for (const i in invReqType) {
        res = invReqType[i].text === val ? invReqType[i].value : res
      }

      return res
    },
    invStepFilter(val) {
      const invStep = category.invStep

      let res = null

      if (val.substring(0, 1) === 'a') {
        for (const i in invStep) {
          res = invStep[i].value === val ? invStep[i].text : res
        }
        return res
      }

      for (const i in invStep) {
        res = invStep[i].text === val ? invStep[i].value : res
      }

      return res
    },
    setAdmin() {
      const accountInfo = JSON.parse(localStorage.getItem('accountInfo'))
      this.$axios
        .post('/api/inv/list', JSON.stringify(accountInfo))
        .then((res) => {
          this.setInv(res.data.invList)
        })
        .catch((err) => {
          console.error(err)
        })
      if (localStorage.getItem('account') !== null) {
        this.adminOn = !!(localStorage.getItem('account') === 'admin')
      }
      return this.adminOn
    },
    setInv(invList) {
      for (const i in invList) {
        invList[i].invStep = this.invStepFilter(invList[i].invStep)
        invList[i].invType = this.invReqTypeFilter(invList[i].invType)
      }

      this.items = invList
    },
    getSelectedRow(val) {
      this.setSeletedRow(val)
      this.dialog = true
    },
    setSeletedRow(selectedRow) {
      this.selectedRow = this.clone(selectedRow)
      this.selectedRow.invType = this.invReqTypeFilter(this.selectedRow.invType)
      this.selectedRow.invStep = this.invStepFilter(this.selectedRow.invStep)
    },
    callBackSelectedRow(res) {},
    getColor(step) {
      let color = 'green'

      switch (step) {
        case '접수':
          color = ''
          break
        case '검토중':
          color = '#EF6C00'
          break
        case '수락':
          color = '#2E7D32'
          break
        case '반려':
          color = '#AD1457'
          break
        case '수정요청':
          color = '#0277BD'
          break
        case '제안취소':
          color = '#5D4037'
          break

        default:
          break
      }
      return color
    },
    clone(obj) {
      if (obj === null || typeof obj !== 'object') return obj

      const copy = obj.constructor()

      for (const attr in obj) {
        // eslint-disable-next-line no-prototype-builtins
        if (obj.hasOwnProperty(attr)) {
          copy[attr] = this.clone(obj[attr])
        }
      }

      return copy
    }
  }
}
</script>

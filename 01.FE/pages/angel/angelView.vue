<template>
  <v-card class="mx-auto" shaped elevation="5">
    <v-card-text>
      <v-container>
        <v-row>
          <v-col cols="4">
            <h4>| 기본 정보</h4>
            <div style="margin: 25px;"></div>

            <v-text-field
              v-model="angel.coNameKor"
              label="회사명(한글)"
              placeholder="회사명"
              :prepend-icon="icons.mdiCityVariantOutline"
              dense
              outlined
              readonly
            ></v-text-field>

            <v-text-field
              v-model="angel.coNameEng"
              class="caption"
              label="회사명(영문)"
              placeholder="회사명"
              :prepend-icon="icons.mdiCityVariant"
              dense
              outlined
              readonly
            ></v-text-field>

            <v-text-field
              v-model="angel.representativeNameKor"
              label="대표자명(한글)"
              placeholder="대표자명"
              :prepend-icon="icons.mdiAccountEdit"
              dense
              outlined
              readonly
            ></v-text-field>

            <v-text-field
              v-model="angel.representativeNameEng"
              class="caption"
              label="대표자명(영문)"
              placeholder="대표자명"
              :prepend-icon="icons.mdiAccountEditOutline"
              dense
              outlined
              readonly
            ></v-text-field>

            <v-text-field
              v-model="angel.foundedDate"
              class="caption"
              label="설립일"
              placeholder="설립일"
              prepend-icon="event"
              dense
              outlined
              readonly
            ></v-text-field>

            <v-textarea
              v-model="angel.coAddr"
              class="caption"
              label="본사위치"
              placeholder="본사위치"
              prepend-icon="place"
              dense
              outlined
              rows="2"
              readonly
            ></v-textarea>

            <v-text-field
              v-model="angel.coWeb"
              class="caption"
              label="웹사이트"
              placeholder="웹사이트"
              prepend-icon="mdi-dialpad"
              dense
              outlined
              readonly
            ></v-text-field>

            <v-text-field
              v-model="angel.coLogo"
              class="caption"
              label="로고"
              placeholder="로고"
              prepend-icon="qwe"
              dense
              outlined
              readonly
            ></v-text-field>
          </v-col>

          <v-col cols="3">
            <h4>| 기업 유형</h4>
            <div style="margin: 25px;"></div>
            <v-subheader>
              <v-icon left>{{ icons.mdiCity }}</v-icon
              >기업 분류
            </v-subheader>
            <v-chip class="ma-2" color="success">
              <v-icon left>{{ icons.mdiBorderColor }}</v-icon>
              {{ angel.corpDiv | corpDivFilter }}</v-chip
            >
            <v-chip class="ma-2" color="red">
              <v-icon left>{{ icons.mdiCheckAll }}</v-icon
              >{{ angel.coStatus | coStatusFilter }}</v-chip
            >
            <v-divider></v-divider>

            <v-subheader>
              <v-icon left>{{ icons.mdiCreation }}</v-icon
              >업무 분야
            </v-subheader>
            <v-chip class="ma-2" color="cyan" pill>
              <v-icon left>{{ icons.mdiBorderColor }}</v-icon>
              {{ angel.largeField | largeFieldFilter }}</v-chip
            >
            <v-divider></v-divider>

            <v-subheader
              ><v-icon left>{{ icons.mdiBrightness5 }}</v-icon> 투자 유형 대분류
            </v-subheader>
            <v-chip class="ma-2" color="pink" text-color="white" pill>
              <v-icon left>{{ icons.mdiBorderColor }}</v-icon>
              {{ angel.invTypeL | invTypeFilter }}</v-chip
            >
            <v-divider></v-divider>

            <v-subheader>
              <v-icon left>{{ icons.mdiBrightness6 }}</v-icon
              >투자 유형 소분류
            </v-subheader>
            <v-chip class="ma-2" color="primary" pill default>
              <v-icon left>{{ icons.mdiBorderColor }}</v-icon>
              {{ angel.invTypeS | invCompTypeFilter }}</v-chip
            >
          </v-col>

          <v-col v-show="!payOn" cols="5">
            <div class="message">
              세부정보는 이용권 구매후 열람가능합니다.
            </div>
          </v-col>

          <v-col v-if="payOn" cols="5">
            <h4>| 투자 정보</h4>
            <div style="margin: 25px;"></div>

            <v-row>
              <v-col>
                <v-text-field
                  v-model="angel.hopCotype01"
                  class="caption"
                  label="희망 기업형태: 01"
                  placeholder="희망 기업형태: 01"
                  :prepend-icon="icons.mdiCheck"
                  dense
                  outlined
                  readonly
                ></v-text-field>
              </v-col>
              <v-col>
                <v-text-field
                  v-model="angel.hopCotype02"
                  class="caption"
                  label="희망 기업형태: 02"
                  placeholder="희망 기업형태: 02"
                  :prepend-icon="icons.mdiCheck"
                  dense
                  outlined
                  readonly
                ></v-text-field>
              </v-col>
            </v-row>

            <v-row>
              <v-col>
                <v-text-field
                  v-model="angel.hopCoSect01"
                  class="caption"
                  label="희망업종: 01"
                  placeholder="희망업종: 01"
                  :prepend-icon="icons.mdiCheckAll"
                  dense
                  outlined
                  readonly
                ></v-text-field>
              </v-col>
              <v-col>
                <v-text-field
                  v-model="angel.hopCoSect02"
                  class="caption"
                  label="희망업종: 02"
                  placeholder="희망업종: 02"
                  :prepend-icon="icons.mdiCheckAll"
                  dense
                  outlined
                  readonly
                ></v-text-field>
              </v-col>
            </v-row>

            <v-row>
              <v-col>
                <v-text-field
                  v-model="angel.hopCoAddr01"
                  class="caption"
                  label="희망소재지: 01"
                  placeholder="희망소재지: 01"
                  prepend-icon="place"
                  dense
                  outlined
                  readonly
                ></v-text-field>
              </v-col>
              <v-col>
                <v-text-field
                  v-model="angel.hopCoAddr02"
                  class="caption"
                  label="희망소재지: 02"
                  placeholder="희망소재지: 02"
                  prepend-icon="place"
                  dense
                  outlined
                  readonly
                ></v-text-field>
              </v-col>
            </v-row>

            <v-textarea
              v-model="angel.hopCoItem"
              class="caption"
              label="희망아이템"
              placeholder="희망아이템"
              :prepend-icon="icons.mdiShapePlus"
              dense
              outlined
              rows="2"
              readonly
            ></v-textarea>

            <v-card class="mx-auto" outlined>
              <v-card-text>
                <v-row no-gutters>
                  <v-col cols="4" class="text-center"
                    ><v-icon>{{ icons.mdiSproutOutline }}</v-icon>
                  </v-col>

                  <v-col cols="2" align="center"
                    ><p style="font-size: 11px;">1억 이하</p>
                  </v-col>
                  <v-col cols="2" align="center"
                    ><p style="font-size: 11px;">1 ~ 5 억</p>
                  </v-col>
                  <v-col cols="2" align="center"
                    ><p style="font-size: 11px;">5 ~ 10 억</p>
                  </v-col>
                  <v-col cols="2" align="center"
                    ><p style="font-size: 11px;">10억 이상</p>
                  </v-col>
                </v-row>

                <v-row no-gutters align="center">
                  <v-col class="text-center" style="font-size: 12px;" cols="4">
                    투자 희망금액
                  </v-col>
                  <v-col cols="2">
                    <v-sheet
                      v-show="angel.hopInvAmount === '01'"
                      color="grey lighten-3"
                      width="100%"
                      height="20"
                    ></v-sheet> </v-col
                  ><v-col cols="2">
                    <v-sheet
                      v-show="angel.hopInvAmount === '02'"
                      color="grey lighten-1"
                      width="100%"
                      height="20"
                    ></v-sheet>
                  </v-col>
                  <v-col cols="2">
                    <v-sheet
                      v-show="angel.hopInvAmount === '03'"
                      color="success lighten-2"
                      width="100%"
                      height="20"
                    ></v-sheet>
                  </v-col>
                  <v-col cols="2">
                    <v-sheet
                      v-show="angel.hopInvAmount === '04'"
                      color="teal lighten-2"
                      width="100%"
                      height="20"
                    ></v-sheet>
                  </v-col>
                </v-row>

                <v-row no-gutters align="center">
                  <v-col class="text-center" style="font-size: 12px;" cols="4">
                    연간매출 희망금액
                  </v-col>
                  <v-col cols="2">
                    <v-sheet
                      v-show="angel.hopSalesVolume === '01'"
                      color="grey lighten-3"
                      width="100%"
                      height="20"
                    ></v-sheet> </v-col
                  ><v-col cols="2">
                    <v-sheet
                      v-show="angel.hopSalesVolume === '02'"
                      color="grey lighten-1"
                      width="100%"
                      height="20"
                    ></v-sheet>
                  </v-col>
                  <v-col cols="2">
                    <v-sheet
                      v-show="angel.hopSalesVolume === '03'"
                      color="success lighten-2"
                      width="100%"
                      height="20"
                    ></v-sheet>
                  </v-col>
                  <v-col cols="2">
                    <v-sheet
                      v-show="angel.hopSalesVolume === '04'"
                      color="teal lighten-2"
                      width="100%"
                      height="20"
                    ></v-sheet>
                  </v-col>
                </v-row>

                <v-row no-gutters align="center">
                  <v-col class="text-center" style="font-size: 12px;" cols="4">
                    영업이익 희망금액
                  </v-col>
                  <v-col cols="2">
                    <v-sheet
                      v-show="angel.hopOpProfit === '01'"
                      color="grey lighten-3"
                      width="90%"
                      height="20"
                    ></v-sheet> </v-col
                  ><v-col cols="2">
                    <v-sheet
                      v-show="angel.hopOpProfit === '02'"
                      color="grey lighten-1"
                      width="100%"
                      height="20"
                    ></v-sheet>
                  </v-col>
                  <v-col cols="2">
                    <v-sheet
                      v-show="angel.hopOpProfit === '03'"
                      color="success lighten-2"
                      width="100%"
                      height="20"
                    ></v-sheet>
                  </v-col>
                  <v-col cols="2">
                    <v-sheet
                      v-show="angel.hopOpProfit === '04'"
                      color="teal lighten-2"
                      width="100%"
                      height="20"
                    ></v-sheet>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
            <v-spacer></v-spacer>
          </v-col>
        </v-row>

        <v-btn
          v-show="payOn && cpnOn && human.accountType === '02'"
          block
          color="#0D47A1"
          @click="
            $router.push({
              path: '/investment/invReg',
              query: {
                angel: angel,
                human: human,
                invType: 'h0'
              }
            })
          "
        >
          {{ angel.coNameKor }}에 투자유치신청
        </v-btn>

        <v-btn v-show="payOn && !cpnOn" block color="#0D47A1" disabled>
          업체 정보를 등록하시면 {{ angel.coNameKor }}에 투자유치를 신청 할 수
          있습니다.
        </v-btn>
      </v-container>
    </v-card-text>
  </v-card>
</template>

<script>
import {
  mdiBorderColor,
  mdiCity,
  mdiCheckAll,
  mdiCreation,
  mdiBrightness5,
  mdiBrightness6,
  mdiCityVariantOutline,
  mdiCityVariant,
  mdiAccountEdit,
  mdiAccountEditOutline,
  mdiCheck,
  mdiShapePlus,
  mdiSproutOutline
} from '@mdi/js'
import category from '~/pages/sample/category'

export default {
  filters: {
    corpDivFilter(val) {
      const corpDivArr = category.corpDivArr

      let res = null
      for (const i in corpDivArr) {
        res = corpDivArr[i].value === val ? corpDivArr[i].text : res
      }

      return res
    },
    coStatusFilter(val) {
      const coStatusArr = category.coStatusArr

      let res = null
      for (const i in coStatusArr) {
        res = coStatusArr[i].value === val ? coStatusArr[i].text : res
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
    invTypeFilter(val) {
      const invType = category.invType

      let res = null
      for (const i in invType) {
        res = invType[i].value === val ? invType[i].text : res
      }

      return res
    },
    invCompTypeFilter(val) {
      const invCompType = category.invCompType

      let res = null
      for (const i in invCompType) {
        res = invCompType[i].value === val ? invCompType[i].text : res
      }

      return res
    }
  },
  data() {
    return {
      payOn: false,
      cpnOn: false,
      icons: {
        mdiBorderColor,
        mdiCity,
        mdiCheckAll,
        mdiCreation,
        mdiBrightness5,
        mdiBrightness6,

        mdiCityVariantOutline,
        mdiCityVariant,
        mdiAccountEdit,
        mdiAccountEditOutline,

        mdiCheck,
        mdiShapePlus,
        mdiSproutOutline
      },
      angel: {},
      human: {},
      angelInv: []
    }
  },
  computed: {
    tokenState() {
      return this.$store.state.payOn.payOn
    }
  },
  watch: {
    flap() {
      this.flap
        ? (this.panel = [...Array(this.items.length).keys()].map((k, i) => k))
        : (this.panel = [])
    },
    tokenState(newTokenState, oldTokenState) {
      this.payOn = newTokenState
    }
  },
  created() {
    let serial = 'nrdywNqcFiczQJx'
    if (this.$route.query.aSerial) serial = this.$route.query.aSerial

    /* 
    ================================================================================================
      데이터 받아오기
    ================================================================================================
    */
    const aSerial = { aSerial: serial } /* TEST: 'nrdywNqcFiczQJx' */

    this.$axios
      .post('/api/angel/detail', JSON.stringify(aSerial))
      .then((res) => {
        this.angel = res.data[0][0]
        this.angelInv = res.data[1]
        this.angel.foundedDate = this.unixTimeFilter(this.angel.foundedDate)

        this.angel.hopCoAddr01 = this.hopCoAddrFilter(this.angel.hopCoAddr01)
        this.angel.hopCoAddr02 = this.hopCoAddrFilter(this.angel.hopCoAddr02)

        this.angel.hopCoSect01 = this.hopCoSectFilter(this.angel.hopCoSect01)
        this.angel.hopCoSect02 = this.hopCoSectFilter(this.angel.hopCoSect02)

        this.angel.hopCotype01 = this.hopCoTypeFilter(this.angel.hopCotype01)
        this.angel.hopCotype02 = this.hopCoTypeFilter(this.angel.hopCotype02)
      })
      .catch((err) => {
        console.error(err)
      })
  },
  mounted() {
    this.payOn = this.$store.state.payOn.payOn
    if (!this.setAdmin()) this.setInvestment()
  },
  methods: {
    setAdmin() {
      if (localStorage.getItem('account') !== null) {
        this.cpnOn = !!(localStorage.getItem('account') === 'admin')
      }
      return this.cpnOn
    },
    setInvestment() {
      if (localStorage.getItem('accountInfo') !== null) {
        const accountInfo = JSON.parse(localStorage.getItem('accountInfo'))
        this.cpnOn = !!accountInfo.accountCo
        this.human = accountInfo
      }
    },
    prcsInvestment() {
      this.$router.push({
        path: '/investment/invReg',
        query: { hSerial: this.human.hSerial }
      })
    },
    unixTimeFilter(val) {
      const date = new Date(val + 1000)
        .toISOString()
        .slice(0, 19)
        .replace('T', ' ')
      return date.substring(0, 10)
    },
    hopInvAmountFilter(val) {
      const hopInvAmount = category.hopInvAmount

      let res = null
      for (const i in hopInvAmount) {
        res = hopInvAmount[i].value === val ? hopInvAmount[i].text : res
      }

      return res
    },
    hopCoTypeFilter(val) {
      const hopCoType = category.corpDivArr

      let res = null
      for (const i in hopCoType) {
        res = hopCoType[i].value === val ? hopCoType[i].text : res
      }

      return res
    },
    hopCoSectFilter(val) {
      const hopCoSect = category.largeField

      let res = null
      for (const i in hopCoSect) {
        res = hopCoSect[i].value === val ? hopCoSect[i].text : res
      }

      return res
    },
    hopCoAddrFilter(val) {
      const hopCoAddr = category.hopCoAddr

      let res = null
      for (const i in hopCoAddr) {
        res = hopCoAddr[i].value === val ? hopCoAddr[i].text : res
      }

      return res
    }
  }
}
</script>

<style>
.chart {
  display: block;
  max-width: 100%;
  max-height: 100%;
  width: auto;
  height: auto;
  color: white;
}

.message {
  position: relative;
  top: 50%;
  left: 75%;
  transform: translate(-50%, -50%);
}
</style>

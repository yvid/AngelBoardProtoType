<template>
  <v-container fluid>
    <v-data-iterator
      style="white-space: pre-line;"
      :items="items"
      :items-per-page.sync="itemsPerPage"
      :page="page"
      :search="search"
      :sort-by="sortBy.toLowerCase()"
      :sort-desc="sortDesc"
      no-data-text="
      
      
      
      찾는 결과가 없습니다."
      no-results-text="
      
      
      
      찾는 결과가 없습니다."
      hide-default-footer
    >
      <template v-slot:header>
        <v-row class="mt-2 stick top" align="center" justify="center">
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
            <template v-if="$vuetify.breakpoint.mdAndUp">
              <v-spacer></v-spacer>
              <v-select
                v-model="sortBy"
                flat
                solo-inverted
                hide-details
                :items="keys"
                prepend-inner-icon="search"
                label="Sort by"
              ></v-select>
              <v-spacer></v-spacer>
              <v-btn-toggle v-model="sortDesc" mandatory>
                <v-btn large depressed color="blue" :value="false">
                  <v-icon>mdi-arrow-up</v-icon>
                </v-btn>
                <v-btn large depressed color="blue" :value="true">
                  <v-icon>mdi-arrow-down</v-icon>
                </v-btn>
              </v-btn-toggle>
            </template>
          </v-toolbar>
        </v-row>
      </template>

      <template v-slot:default="props">
        <v-row style="padding-top: 60px; padding-bottom: 100px; width: 65vw;">
          <v-col
            v-for="item in props.items"
            :key="item.key"
            cols="12"
            sm="6"
            md="4"
            lg="3"
          >
            <v-card class="mx-auto my-1" max-width="374">
              <v-card-text>
                <v-row align="center" class="mx-0">
                  <v-rating
                    :value="4.5"
                    color="amber"
                    dense
                    half-increments
                    readonly
                    size="14"
                  ></v-rating>

                  <div class="grey--text ml-4">조회 평점: 4.5</div>
                </v-row>

                <div
                  v-for="(key, index) in filteredKeys"
                  :key="index"
                  :class="{ 'blue--text': sortBy === key }"
                >
                  <div v-if="index === 1" class="my-2 subtitle-3">
                    <v-icon dense small>{{
                      icons.mdiCityVariantOutline
                    }}</v-icon>
                    {{ item[key.toLowerCase()] }}
                  </div>

                  <div v-if="index === 0" class="my-2 subtitle-2">
                    <v-icon dense small>{{ icons.mdiCityVariant }}</v-icon>
                    {{ item[key.toLowerCase()] }}
                  </div>

                  <div
                    v-if="index === 2"
                    class="caption"
                    style="min-height:22px; max-height:60px; overflow:auto;"
                  >
                    <div>
                      <v-icon dense small>{{
                        icons.mdiChatProcessingOutline
                      }}</v-icon>
                      {{ item[key.toLowerCase()] }}
                    </div>
                  </div>
                  <v-divider class="mx-4"></v-divider>
                </div>

                <div class="my-2 caption">
                  선호기업 형태
                  <v-chip-group
                    active-class="deep-purple accent-4 white--text"
                    column
                  >
                    <v-chip small>{{
                      item.hopCotype01 | hopCotypeFilter
                    }}</v-chip>
                    <v-chip small>{{
                      item.hopCotype02 | hopCotypeFilter
                    }}</v-chip>
                  </v-chip-group>
                </div>
                <div class="my-1 caption">
                  선호기업 업종
                  <v-chip-group
                    active-class="deep-purple accent-4 white--text"
                    column
                  >
                    <v-chip small>{{
                      item.hopCoSect01 | hopCoSectFilter
                    }}</v-chip>
                    <v-chip small>{{
                      item.hopCoSect02 | hopCoSectFilter
                    }}</v-chip>
                  </v-chip-group>

                  <v-card-actions>
                    <v-btn
                      text
                      color="deep-purple accent-1"
                      @click="
                        $router.push({
                          path: `/angel/angelView`,
                          query: { aSerial: item.aSerial }
                        })
                      "
                    >
                      More...
                    </v-btn>
                  </v-card-actions>
                </div>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </template>

      <template v-slot:footer>
        <v-row
          class="mt-2 grey darken-3 stick bottom pa-1"
          align="center"
          justify="center"
        >
          <span class="white--text">Item Per Page</span>
          <v-menu offset-y>
            <template v-slot:activator="{ on }">
              <v-btn dark text color="primary" class="ml-2" v-on="on">
                {{ itemsPerPage }}
                <v-icon>mdi-chevron-down</v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-item
                v-for="(number, index) in itemsPerPageArray"
                :key="index"
                @click="updateItemsPerPage(number)"
              >
                <v-list-item-title>{{ number }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>

          <v-spacer></v-spacer>

          <span
            class="mr-4
            grey--text"
          >
            Page {{ page }} of {{ numberOfPages }}
          </span>
          <v-btn
            fab
            dark
            color="blue darken-3"
            class="mr-1"
            @click="formerPage"
          >
            <v-icon>mdi-chevron-left</v-icon>
          </v-btn>
          <v-btn fab dark color="blue darken-3" class="ml-1" @click="nextPage">
            <v-icon>mdi-chevron-right</v-icon>
          </v-btn>
        </v-row>
      </template>
    </v-data-iterator>
  </v-container>
</template>

<script>
import {
  mdiCityVariant,
  mdiCityVariantOutline,
  mdiChatProcessingOutline
} from '@mdi/js'
import category from '~/pages/sample/category'

export default {
  filters: {
    hopCotypeFilter(val) {
      const hopCotype = category.corpDivArr

      let res = null
      for (const i in hopCotype) {
        res = hopCotype[i].value === val ? hopCotype[i].text : res
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
    }
  },
  data() {
    return {
      icons: {
        mdiCityVariant,
        mdiCityVariantOutline,
        mdiChatProcessingOutline
      },
      itemsPerPageArray: [4, 8, 12, 48, 80],
      search: '',
      filter: {},
      sortDesc: false,
      page: 1,
      itemsPerPage: 8,
      sortBy: '회사명(한글)',
      keys: ['회사명(한글)', '회사명(영문)', '기업소개'],
      items: []
    }
  },
  computed: {
    numberOfPages() {
      return Math.ceil(this.items.length / this.itemsPerPage)
    },
    filteredKeys() {
      return this.keys.filter((key) => key !== `Name`)
    }
  },
  created() {
    this.$axios
      .post('/api/angel/list')
      .then((res) => {
        this.items = res.data[0]
      })
      .catch((err) => {
        throw err
      })
  },
  methods: {
    nextPage() {
      if (this.page + 1 <= this.numberOfPages) this.page += 1
    },
    formerPage() {
      if (this.page - 1 >= 1) this.page -= 1
    },
    updateItemsPerPage(number) {
      this.itemsPerPage = number
    }
  }
}
</script>

<style scoped>
.stick {
  position: fixed;
  z-index: 100;
  width: 65vw;
}
.top {
  top: 65px;
}
.bottom {
  bottom: 40px;
}
</style>

<template>
  <v-layout justify-center>
    <v-flex xs12 sm10 md8 lg8>
      <v-card class="overflow-hidden">
        <v-app-bar
          absolute
          elevate-on-scroll
          dark
          dense
          flat
          scroll-target="#scrolling-techniques"
        >
          <template v-slot:extension>
            <v-tabs v-model="tabs" centered :grow="true">
              <v-tab v-for="item in items" :key="item.id" @click="scrollMove">
                {{ item.name }}
              </v-tab>
            </v-tabs>
          </template>
          <v-toolbar-title @click="setSample()">정보 등록</v-toolbar-title>
          <v-spacer></v-spacer>
          <span style="color: #BBDEFB; font-size:13px;">{{ notice }}</span>
        </v-app-bar>
        <v-sheet
          id="scrolling-techniques"
          ref="sheet"
          class="overflow-y-auto"
          max-height="750"
        >
          <v-container style="height: 1000px; margin-top:100px;">
            <v-tabs-items v-model="tabs">
              <!-- tab-1 start -->
              <v-tab-item>
                <v-card flat>
                  <v-card-text>
                    <v-text-field
                      ref="regTel"
                      v-model="angel.regTel"
                      :rules="[() => !!angel.regTel || '필수 입력!']"
                      :error-messages="errorMessages"
                      label="* 등록자 연락처(숫자만 입력)"
                      placeholder="연락처를 입력해주세요"
                      required
                      @keyup="angel.regTel = typingNum($event.target.value, 15)"
                    ></v-text-field>

                    <v-text-field
                      ref="regEMailID"
                      v-model.lazy="angel.regEmailId"
                      :rules="[() => !!angel.regEmailId || '필수 입력!']"
                      :error-messages="errorMessages"
                      label="* 등록자 이메일"
                      placeholder="이메일 계정을 입력해주세요"
                      disabled
                      required
                      @blur="angel.regEmailId = checkEmail($event.target.value)"
                    ></v-text-field>

                    <v-text-field
                      ref="regContPwd"
                      v-model="angel.regContPwd"
                      :append-icon="show ? 'visibility' : 'visibility_off'"
                      :type="show ? 'text' : 'password'"
                      :rules="[() => !!angel.regContPwd || '필수 입력!']"
                      name="input-10-2"
                      :error-messages="errorMessages"
                      label="* 회사정보 관리 비밀번호 (최소 6자리)"
                      placeholder=""
                      class="input-group--focused"
                      required
                      @click:append="show = !show"
                    ></v-text-field>

                    <v-text-field
                      ref="coNameKor"
                      v-model="angel.coNameKor"
                      :rules="[() => !!angel.coNameKor || '필수 입력!']"
                      :error-messages="errorMessages"
                      label="* 회사명(한글) - 주식회사의 경우 법인등기명칭으로 입력"
                      placeholder="한글 회사명을 입력해주세요"
                      required
                      @keyup="angel.coNameKor = typingKor($event.target.value)"
                    ></v-text-field>

                    <v-text-field
                      ref="coNameEng"
                      v-model="angel.coNameEng"
                      :rules="[() => !!angel.coNameEng || '필수 입력!']"
                      :error-messages="errorMessages"
                      label="* 회사명(영문)"
                      placeholder="영문 회사명을 입력해주세요"
                      @keyup="angel.coNameEng = typingEng($event.target.value)"
                    ></v-text-field>

                    <v-text-field
                      ref="representativeNameKor"
                      v-model="angel.representativeNameKor"
                      :rules="[
                        () => !!angel.representativeNameKor || '필수 입력!'
                      ]"
                      :error-messages="errorMessages"
                      label="* 대표자명 - 한글"
                      placeholder="한글 대표자명을 입력해주세요"
                      required
                      @keyup="
                        angel.representativeNameKor = typingKor(
                          $event.target.value
                        )
                      "
                    ></v-text-field>

                    <v-text-field
                      ref="representativeNameEng"
                      v-model="angel.representativeNameEng"
                      :rules="[
                        () => !!angel.representativeNameEng || '필수 입력!'
                      ]"
                      :error-messages="errorMessages"
                      label="* 대표자명 - 영문"
                      placeholder="영문 대표자명을 입력해주세요"
                      required
                      @keyup="
                        angel.representativeNameEng = typingEng(
                          $event.target.value
                        )
                      "
                    ></v-text-field>

                    <v-text-field
                      ref="coTel"
                      v-model="angel.coTel"
                      :rules="[() => !!angel.coTel || '필수 입력!']"
                      :error-messages="errorMessages"
                      label="* 회사 연락처(숫자만 입력)"
                      required
                      placeholder="회사 연락처를 입력해주세요"
                      @keyup="angel.coTel = typingNum($event.target.value, 15)"
                    ></v-text-field>

                    <v-menu
                      ref="datePick01"
                      v-model="datePick01"
                      :close-on-content-click="false"
                      :return-value.sync="angel.foundedDate"
                      transition="scale-transition"
                      offset-y
                      min-width="290px"
                    >
                      <template v-slot:activator="{ on }">
                        <v-text-field
                          v-model="angel.foundedDate"
                          label="* 설립일: 선택"
                          prepend-icon="event"
                          readonly
                          v-on="on"
                        ></v-text-field>
                      </template>
                      <v-date-picker
                        v-model="angel.foundedDate"
                        no-title
                        scrollable
                      >
                        <v-spacer></v-spacer>
                        <v-btn text color="primary" @click="datePick01 = false"
                          >취소</v-btn
                        >
                        <v-btn
                          text
                          color="primary"
                          @click="$refs.datePick01.save(angel.foundedDate)"
                          >선택</v-btn
                        >
                      </v-date-picker>
                    </v-menu>

                    <v-chip-group>
                      <v-text-field
                        ref="coAddr"
                        v-model="angel.coAddr"
                        :rules="[() => !!angel.coAddr || '필수 입력!']"
                        :error-messages="errorMessages"
                        label="* 본사 주소(전체 주소)"
                        placeholder="전체 주소를 입력해주세요"
                        required
                      ></v-text-field>
                      <v-dialog v-model="dialog" width="500">
                        <template v-slot:activator="{ on }">
                          <v-btn dark v-on="on">
                            검색
                          </v-btn>
                        </template>

                        <v-card>
                          <v-card-title
                            class="headline grey lighten-2"
                            primary-title
                          >
                            주소
                          </v-card-title>
                          <client-only>
                            <vue-daum-postcode
                              style="max-height: 600px; overflow: scroll;"
                              @complete="addrComplete"
                            />
                          </client-only>
                          <v-divider></v-divider>

                          <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn color="primary" text @click="dialog = false">
                              닫기
                            </v-btn>
                          </v-card-actions>
                        </v-card>
                      </v-dialog>
                    </v-chip-group>

                    <v-text-field
                      ref="coWeb"
                      v-model="angel.coWeb"
                      label="회사 웹사이트"
                      placeholder="회사 웹사이트 주소를 입력해주세요"
                    ></v-text-field>

                    <v-text-field
                      ref="coLogo"
                      v-model="angel.coLogo"
                      label="회사로고 링크"
                      placeholder="회사로고 링크 주소를 입력해주세요"
                    ></v-text-field>
                  </v-card-text>
                </v-card>
              </v-tab-item>

              <!-- tab-2 start -->
              <v-tab-item>
                <v-card flat>
                  <v-card-text>
                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* 법인 구분:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="corpDiv"
                          v-model="angel.corpDiv"
                          :rules="[() => !!angel.corpDiv || '필수 입력!']"
                          :items="corpDivArr"
                          label="* 법인 구분"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* 회사 상태:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="coStatus"
                          v-model="angel.coStatus"
                          :rules="[() => !!angel.coStatus || '필수 입력!']"
                          :items="coStatus"
                          label="* 회사 상태"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* 대표 업종:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="largeField"
                          v-model="angel.largeField"
                          :rules="[() => !!angel.largeField || '필수 입력!']"
                          :error-messages="errorMessages"
                          :items="largeField"
                          label="* 대분야"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-textarea
                      ref="smallField"
                      v-model="angel.smallField"
                      :rules="[() => !!angel.smallField || '필수 입력!']"
                      :error-messages="errorMessages"
                      :label="
                        '* 아이템 - 대표 아이템 / 서비스 간략히 기재 (' +
                          countByte(angel.smallField, 400)
                      "
                      required
                      rows="2"
                      auto-grow
                      @keyup="angel.smallField = chkByte(angel.smallField, 400)"
                    ></v-textarea>

                    <v-text-field
                      ref="capital"
                      v-model="angel.capital"
                      :rules="[() => !!angel.capital || '필수 입력!']"
                      :error-messages="errorMessages"
                      label="* 보유현금"
                      required
                      placeholder="보유현금(숫자만 입력)"
                      suffix="원"
                      @keyup="angel.capital = typingCash($event.target.value)"
                    ></v-text-field>

                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* 투자 유형(대분류):</h4></v-col>
                      <v-col
                        ><v-select
                          ref="invTypeL"
                          v-model="angel.invTypeL"
                          :rules="[() => !!angel.invTypeL || '필수 입력!']"
                          :error-messages="errorMessages"
                          :items="invTypeL"
                          label="* 대분류"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* 투자 유형(소분류):</h4></v-col>
                      <v-col
                        ><v-select
                          ref="invTypeS"
                          v-model="angel.invTypeS"
                          :rules="[() => !!angel.invTypeS || '필수 입력!']"
                          :error-messages="errorMessages"
                          :items="invTypeS"
                          label="* 소분류"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>
                  </v-card-text>
                </v-card>
              </v-tab-item>

              <!-- tab-3 start -->
              <v-tab-item>
                <v-card flat>
                  <v-card-text>
                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"
                        ><h4>* 희망 투자유치 기업 형태 1:</h4></v-col
                      >
                      <v-col
                        ><v-select
                          ref="hopCotype01"
                          v-model="angel.hopCotype01"
                          :rules="[() => !!angel.hopCotype01 || '필수 입력!']"
                          :items="hopCotype"
                          label="* 희망 투자유치 기업 형태 선택 1"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"
                        ><h4>* 희망 투자유치 기업 형태 2:</h4></v-col
                      >
                      <v-col
                        ><v-select
                          ref="hopCotype02"
                          v-model="angel.hopCotype02"
                          :rules="[() => !!angel.hopCotype02 || '필수 입력!']"
                          :items="hopCotype"
                          label="* 희망 투자유치 기업 형태 선택 2"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* 희망 투자업종 1:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="hopCoSect01"
                          v-model="angel.hopCoSect01"
                          :rules="[() => !!angel.hopCoSect01 || '필수 입력!']"
                          :error-messages="errorMessages"
                          :items="hopCoSect"
                          label="* 희망 투자업종 1"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* 희망 투자업종 2:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="hopCoSect02"
                          v-model="angel.hopCoSect02"
                          :rules="[() => !!angel.hopCoSect02 || '필수 입력!']"
                          :error-messages="errorMessages"
                          :items="hopCoSect"
                          label="* 희망 투자업종 2"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-textarea
                      ref="hopCoItem"
                      v-model="angel.hopCoItem"
                      :rules="[() => !!angel.hopCoItem || '필수 입력!']"
                      :error-messages="errorMessages"
                      :label="
                        '* 희망 아이템(투자 유치자가 이해 할 수 있도록 간략히 명시) (' +
                          countByte(angel.hopCoItem, 400)
                      "
                      required
                      rows="2"
                      auto-grow
                      @keyup="angel.hopCoItem = chkByte(angel.hopCoItem, 400)"
                    ></v-textarea>

                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* 희망 소재지 1:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="hopCoAddr01"
                          v-model="angel.hopCoAddr01"
                          :rules="[() => !!angel.hopCoAddr01 || '필수 입력!']"
                          :error-messages="errorMessages"
                          :items="hopCoAddr"
                          label="* 대분야"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* 희망 소재지 2:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="hopCoAddr02"
                          v-model="angel.hopCoAddr02"
                          :rules="[() => !!angel.hopCoAddr02 || '필수 입력!']"
                          :error-messages="errorMessages"
                          :items="hopCoAddr"
                          label="* 대분야"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* 희망 투자액:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="hopSalesVolume"
                          v-model="angel.hopInvAmount"
                          :rules="[() => !!angel.hopInvAmount || '필수 입력!']"
                          :error-messages="errorMessages"
                          :items="hopInvAmount"
                          label="* 대분야"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* 희망 연간 매출액:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="hopSalesVolume"
                          v-model="angel.hopSalesVolume"
                          :rules="[
                            () => !!angel.hopSalesVolume || '필수 입력!'
                          ]"
                          :error-messages="errorMessages"
                          :items="hopSalesVolume"
                          label="* 대분야"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* 희망 연간 영업이익:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="hopOpProfit"
                          v-model="angel.hopOpProfit"
                          :rules="[() => !!angel.hopOpProfit || '필수 입력!']"
                          :error-messages="errorMessages"
                          :items="hopOpProfit"
                          label="* 대분야"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-textarea
                      ref="etc"
                      v-model="angel.etc"
                      :rules="[() => !!angel.etc || '필수 입력!']"
                      :error-messages="errorMessages"
                      :label="
                        '* 자사 소개 - 투자자로써 간략한 소개내용 기재 (' +
                          countByte(angel.etc, 400)
                      "
                      required
                      rows="2"
                      auto-grow
                      @keyup="angel.etc = chkByte(angel.etc, 400)"
                    ></v-textarea>
                  </v-card-text>
                </v-card>
              </v-tab-item>

              <!-- tab-4 start -->
              <v-tab-item>
                <v-card flat>
                  <v-card-text>
                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>투자실적 정보 유무:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="invInfo"
                          v-model="angel.invInfo"
                          :rules="[() => !!angel.invInfo || '필수 입력!']"
                          :error-messages="errorMessages"
                          :items="invInfo"
                          label="* 투자실적 정보 유무"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-switch
                      v-if="angel.invInfo === '01'"
                      v-model="angel.invInfoAddIntention"
                      label="'투자실적 정보'를 등록하시겠습니까?"
                    ></v-switch>
                    <div
                      v-if="angel.invInfo === '01' && angel.invInfoAddIntention"
                    >
                      <div
                        class="text-left"
                        style="margin-bottom:20px; margin-top:20px;"
                      >
                        <v-btn
                          small
                          :disabled="invTime < 2"
                          @click="invTimeMinus"
                        >
                          <v-icon>mdi-minus</v-icon>
                        </v-btn>
                        <v-chip label>{{ invTime }} </v-chip>
                        <v-btn small @click="invTimePlus">
                          <v-icon>mdi-plus</v-icon>
                        </v-btn>
                        <span style="font-size: 16px;">투자실적 이력 수</span>
                      </div>

                      <div v-for="(item, i) in invTime" :key="i">
                        <v-divider />
                        <div style="margin-bottom:20px; margin-top:20px;">
                          <v-chip> # 투자실적 이력: {{ item }}</v-chip>
                        </div>

                        <v-menu
                          ref="datePick02"
                          v-model="angel.invArr[i].datePick02"
                          :close-on-content-click="false"
                          :return-value.sync="angel.invArr[i].preInvDate"
                          transition="scale-transition"
                          offset-y
                          min-width="290px"
                        >
                          <template v-slot:activator="{ on }">
                            <v-text-field
                              v-model="angel.invArr[i].preInvDate"
                              label="* 투자날짜: 선택"
                              prepend-icon="event"
                              readonly
                              v-on="on"
                            ></v-text-field>
                          </template>
                          <v-date-picker
                            v-model="angel.invArr[i].preInvDate"
                            no-title
                            scrollable
                          >
                            <v-spacer></v-spacer>
                            <v-btn
                              text
                              color="primary"
                              @click="angel.invArr[i].datePick02 = false"
                              >취소</v-btn
                            >
                            <v-btn
                              text
                              color="primary"
                              @click="
                                $refs.datePick02[i].save(
                                  angel.invArr[i].preInvDate
                                )
                              "
                              >선택</v-btn
                            >
                          </v-date-picker>
                        </v-menu>

                        <v-row class="d-flex align-baseline" no-gutters>
                          <v-col cols="4"><h4>* 투자 단계:</h4></v-col>
                          <v-col
                            ><v-select
                              ref="preInvStage"
                              v-model="angel.invArr[i].preInvStage"
                              :rules="[
                                () =>
                                  !!angel.invArr[i].preInvStage || '필수 입력!'
                              ]"
                              :error-messages="errorMessages"
                              :items="preInvStage"
                              label="* 투자 단계"
                              placeholder="선택.."
                              outlined
                              required
                            ></v-select
                          ></v-col>
                        </v-row>

                        <v-text-field
                          ref="totalInvAmount"
                          v-model="angel.invArr[i].preInvAmount"
                          :rules="[
                            () => !!angel.invArr[i].preInvAmount || '필수 입력!'
                          ]"
                          :error-messages="errorMessages"
                          label="* 투자 금액(억)"
                          required
                          placeholder="억원"
                          suffix="억원"
                          type="number"
                        ></v-text-field>

                        <v-text-field
                          ref="preInvestor"
                          v-model="angel.invArr[i].preInvestor"
                          :rules="[
                            () => !!angel.invArr[i].preInvestor || '필수 입력!'
                          ]"
                          :error-messages="errorMessages"
                          label="* 투자처 (직업입력)"
                          required
                          placeholder="투자처(기업, 기관, 개인) 정보를 입력해주세요"
                        ></v-text-field>
                        <v-divider />
                      </div>
                    </div>
                  </v-card-text>
                </v-card>
              </v-tab-item>
            </v-tabs-items>
          </v-container>
        </v-sheet>

        <div class="text-center">
          <v-row align="center">
            <v-col>
              <v-btn
                v-if="tabs > 0"
                class="ma-2"
                tile
                color="indigo"
                dark
                @click="prevTab"
              >
                <v-icon left>mdi-pencil</v-icon> 이전</v-btn
              >
            </v-col>
            <v-col>
              <v-btn
                v-if="!modify"
                class="ma-2"
                tile
                outlined
                color="gray"
                @click="submit"
              >
                <v-icon>mdi-domain</v-icon> 등록
              </v-btn>
              <v-btn
                v-if="modify"
                class="ma-2"
                tile
                outlined
                color="gray"
                @click="submit"
              >
                <v-icon>mdi-domain</v-icon> 수정
              </v-btn>
            </v-col>
            <v-col>
              <v-btn
                v-if="tabs < 3"
                class="ma-2"
                tile
                outlined
                color="success"
                @click="nextTab"
              >
                <v-icon left>mdi-pencil</v-icon> 다음
              </v-btn>
            </v-col>
            <!-- <v-col>
              <v-btn @click="complete = !complete">다이얼로그 </v-btn>
            </v-col> -->
          </v-row>
        </div>
      </v-card>
    </v-flex>

    <div class="d-flex align-end">
      <div style="margin: 15px;">
        <v-btn
          class="d-none d-lg-flex d-xl-none"
          color="#0D47A1"
          dark
          small
          bottom
          rounded
          @click="scrollTop"
        >
          <v-icon>{{ icons.mdiChevronUp }}</v-icon>
        </v-btn>

        <v-btn
          class="d-none d-lg-flex d-xl-none"
          color="#1E88E5"
          dark
          small
          bottom
          rounded
          @click="scrollBottom"
        >
          <v-icon>{{ icons.mdiChevronDown }}</v-icon>
        </v-btn>
      </div>
    </div>

    <v-dialog v-model="requiredNotice" max-width="400">
      <v-card>
        <v-card-title>
          <span>완료되지 않은 항목이 있습니다.</span>
          <span>필수입력 항목을 확인해주세요.</span>
          <v-spacer></v-spacer>
        </v-card-title>
        <v-card-actions class="d-flex flex-row-reverse">
          <v-btn color="primary" text @click="requiredNotice = false">
            닫기
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="complete" max-width="400">
      <v-card>
        <v-card-title>
          <span v-if="!modify">기업정보 등록이 완료 되었습니다.</span>
          <span v-if="modify">기업정보 수정이 완료 되었습니다.</span>
          <v-spacer></v-spacer>
        </v-card-title>
        <v-card-actions class="d-flex flex-row-reverse">
          <v-btn color="primary" text @click="complete = false">
            페이지가 이동 됩니다.
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<script>
/* 스크롤버튼 화살표 아이콘 */
import { mdiChevronDown, mdiChevronUp } from '@mdi/js'

/* 
'vue-daum-postcode' 주소찾기 Component import : nuxt에서는 새로고침 시 오류
import { VueDaumPostcode } from 'vue-daum-postcode'
 */
import country from '~/pages/sample/country'
import category from '~/pages/sample/category'

/* 아래와 같은 방식으로 주소찾기 Component를 import하면 새로고침 시 오류 해결 */
let VueDaumPostcode
let textEncoder

if (process.client) {
  textEncoder = new TextEncoder()
  VueDaumPostcode = require('vue-daum-postcode')
  /* 
  window.onbeforeunload = function(e) {
    const dialogText = 'Refresh Detected'
    e.returnValue = dialogText
    return dialogText
  }
   */
}

export default {
  components: {
    /* 
    'vue-daum-postcode' 주소찾기 Component import : 아래와 같이 할 경우 nuxt에서는 새로고침 시 오류
    VueDaumPostcode
    */
  },
  data: () => ({
    modify: false,
    icons: {
      mdiChevronDown,
      mdiChevronUp
    },
    notice: '*표시: 필수입력',
    currentComponents: null,
    countries: [],
    tabs: null,
    items: [
      { id: 1, name: '기업 기본 정보' },
      { id: 2, name: '기업 상태 정보' },
      { id: 3, name: '희망 투자유치 기업 정보' },
      { id: 4, name: '기존 투자실적 정보' }
    ],
    text: 'consequat.',
    errorMessages: '',
    show: false,
    dialog: false,
    complete: false,
    requiredNotice: false,
    angel: {
      aSerial: null,

      /* tab-1 */
      regTel: null /* 등록자Tel */,
      regEmailId: null /* 등록자 이메일ID */,
      regContPwd: null /* 정보관리 비밀번호 */,
      coNameKor: null /* 회사 이름 - 한글 */,
      coNameEng: null /* 회사 이름 - 영문 */,
      representativeNameKor: null /* 대표자명 - 한글 */,
      representativeNameEng: null /* 대표자명 - 영문 */,
      coTel: null /* 회사TEL */,
      foundedDate: null /* 설립일 */,
      coAddr: null /* 본사위치 - 법인기준 전체주소 */,
      coWeb: null /* 회사 웹사이트 */,
      coLogo: null /* 회사 로고 - 링크 */,

      /* tab-2 */
      corpDiv: null /* 법인구분 */,
      coStatus: null /* 회사상태 */,
      largeField: null /* 업종 */,
      smallField: null /* 아이템 */,
      capital: null /* 보유현금 */,
      invTypeL: null /* 투자유형(대) */,
      invTypeS: null /* 투자유형(소) */,

      /* tab-3 */
      hopCotype01: null /* 희망 기업형태01 */,
      hopCotype02: null /* 희망 기업형태02 */,
      hopCoSect01: null /* 희망업종01 */,
      hopCoSect02: null /* 희망업종02 */,
      hopCoItem: null /* 희망아이템 */,
      hopCoAddr01: null /* 희망소재지 01 */,
      hopCoAddr02: null /* 희망소재지 02 */,
      hopInvAmount: null /* 희망투자액 */,
      hopSalesVolume: null /* 희망 연간 매출액 */,
      hopOpProfit: null /* 희망 연간 영업이익 */,
      etc: null /* 비고 */,

      /* tab-4 */
      invArr: [
        {
          datePick02: false,
          preInvDate: new Date().toISOString().substr(0, 10),
          preInvTime: 1,
          preInvStage: null,
          preInvAmount: null,
          preInvestor: null
        }
      ],
      invInfo: '02',
      invInfoAddIntention: false,

      regDate: null
    },
    datePick01: false,
    invTime: 1,
    corpDivArr: [],
    coStatus: [],
    largeField: [],
    invTypeL: [],
    invTypeS: [],
    hopCotype: [],
    hopCoSect: [],
    hopCoAddr: [],
    hopInvAmount: [],
    hopSalesVolume: [],
    hopOpProfit: [],
    invInfo: [],
    invInfoAddIntention: [],
    preInvStage: []
  }),
  computed: {
    form() {
      return {
        /* tab-1 */
        regTel: this.angel.regTel,
        regEmailId: this.angel.regEmailId,
        regContPwd: this.angel.regContPwd,
        coNameKor: this.angel.coNameKor,
        coNameEng: this.angel.coNameEng,
        representativeNameKor: this.angel.representativeNameKor,
        representativeNameEng: this.angel.representativeNameEng,
        coTel: this.angel.coTel,
        foundedDate: this.angel.foundedDate,
        coAddr: this.angel.coAddr,

        /* tab-2 */
        corpDiv: this.angel.corpDiv,
        coStatus: this.angel.coStatus,
        largeField: this.angel.largeField,
        smallField: this.angel.smallField,
        capital: this.angel.capital,
        invTypeL: this.angel.invTypeL,
        invTypeS: this.angel.invTypeS,

        /* tab-3 */
        hopCotype01: this.angel.hopCotype01,
        hopCotype02: this.angel.hopCotype02,
        hopCoSect01: this.angel.hopCoSect01,
        hopCoSect02: this.angel.hopCoSect02,
        hopCoItem: this.angel.hopCoItem,
        hopCoAddr01: this.angel.hopCoAddr01,
        hopCoAddr02: this.angel.hopCoAddr02,
        hopInvAmount: this.angel.hopInvAmount,
        hopSalesVolume: this.angel.hopSalesVolume,
        hopOpProfit: this.angel.hopOpProfit

        /* tab-4 */
      }
    }
  },
  watch: {
    dialog(val) {
      if (val) {
        this.currentComponents = VueDaumPostcode
      } else {
        this.currentComponents = null
      }
    }
  },
  created() {
    /* 국가 select 데이터 바인딩 */
    this.countries = country.countries

    /* 카테고리(Select Box)데이터 바인딩 */
    this.corpDivArr = category.corpDivArr
    this.coStatus = category.coStatusArr
    this.largeField = category.largeField
    this.invTypeL = category.invType
    this.invTypeS = category.invCompType
    this.hopCotype = category.corpDivArr
    this.hopCoSect = category.largeField
    this.hopCoAddr = category.hopCoAddr
    this.hopInvAmount = category.hopInvAmount
    this.hopSalesVolume = category.hopInvAmount
    this.hopOpProfit = category.hopInvAmount
    this.invInfo = category.invInfo
    this.invInfoAddIntention = category.invInfoAddIntention
    this.preInvStage = category.preInvStage
  },

  mounted() {
    if (localStorage.getItem('account') !== null) {
      this.angel.regEmailId = localStorage.getItem('account')
      this.getAccountCompSerial(JSON.parse(localStorage.getItem('accountInfo')))
    }
  },
  methods: {
    getAccountCompSerial(accountInfo) {
      if (accountInfo.accountCo !== '' && accountInfo.accountCo !== null) {
        this.modify = true
        this.$axios
          .post(
            '/api/angel/detail',
            JSON.stringify({ aSerial: accountInfo.accountCo })
          )
          .then((res) => {
            this.invTime = res.data[1].length
            this.angel = res.data[0][0]
            this.angel.invArr = res.data[1]

            this.angel.foundedDate = this.unixTimeFilter(this.angel.foundedDate)
            this.angel.capital = this.typingCash(this.angel.capital.toString())
            this.angel.coTel = '0' + this.angel.coTel.toString()
            this.angel.regTel = '0' + this.angel.regTel.toString()

            for (const i in this.angel.invArr) {
              this.angel.invArr[i].preInvDate = this.unixTimeFilter(
                this.angel.invArr[i].preInvDate
              )
            }
          })
          .catch((err) => {
            console.error(err)
          })
      }
    },

    /* 
    ================================================================================================
      입력 기능
    ================================================================================================
    */

    /* 탭 선택시 스크롤 상단 */
    scrollMove() {
      this.$refs.sheet.$el.scrollTop = 0
    },

    /* 스크롤 위로 버튼 */
    scrollTop() {
      this.scrollMove()
    },

    /* 스크롤 아래로 버튼 */
    scrollBottom() {
      this.$refs.sheet.$el.scrollTop = this.$refs.sheet.$el.scrollHeight
    },

    /* 주소 API 선택 후 변수에 적용 */
    addrComplete(res) {
      this.angel.coAddr = res.address
      this.dialog = false
    },

    /* 입력항목 탭이동 '이전', '다음' */
    nextTab(tab) {
      this.tabs = this.tabs + 1
      this.scrollMove()
    },
    prevTab(tab) {
      this.tabs = this.tabs - 1
      this.scrollMove()
    },

    /* 한글, 영문, 숫자, 금액만 입력 가능하게 필터링 */
    typingKor(e) {
      const pattern = /[a-zA-Z]/
      return e.replace(pattern, '')
    },
    typingEng(e) {
      const pattern = /[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]/
      return e.replace(pattern, '')
    },
    typingNum(e, byte) {
      const pattern = /[^0-9]/
      return this.chkByte(e.replace(pattern, ''), byte)
    },
    typingCash(e) {
      const pattern = /[^0-9]/

      let res = e.replace(pattern, '')
      res = res.replace(/,/g, '')
      res = res.replace(/\B(?=(\d{3})+(?!\d))/g, ',')
      return res
    },

    /* 이메일형식 입력 확인 */
    checkEmail(email) {
      const pattern = /^(([^<>()\\[\]\\.,;:\s@"]+(\.[^<>()\\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/
      if (pattern.test(email) === false) {
        // 이메일 형식이 알파벳+숫자@알파벳+숫자.알파벳+숫자 형식이 아닐경우
        return ''
      }
      return email
    },

    /* 기존 투자정보 삭제/추가 기능 */
    invTimeMinus() {
      this.angel.invArr.splice(this.invTime - 1)
      this.invTime--
    },
    invTimePlus() {
      this.angel.invArr[this.invTime] = {
        preInvDate: new Date().toISOString().substr(0, 10),
        preInvTime: this.invTime + 1,
        preInvStage: null,
        preInvAmount: null,
        preInvestor: null
      }

      this.invTime++
    },

    /* Text Area Byte제한 필터링 */
    countByte(val, bytes) {
      if (textEncoder)
        return textEncoder.encode(val).length + '/ ' + bytes + 'bytes)'
    },
    chkByte(obj, bytes) {
      /* const char = new TextEncoder().encode(obj).length 전체 바이트 수 한번에 구할 때 사용 */

      if (obj == null || obj.length === 0) {
        return null
      }

      let size = 0
      let rIndex = obj.length

      for (let i = 0; i < obj.length; i++) {
        size += this.charByteSize(obj.charAt(i))
        if (size === bytes) {
          rIndex = i + 1
          break
        } else if (size > bytes) {
          rIndex = i
          break
        }
      }

      return obj.substring(0, rIndex)
    },
    charByteSize(ch) {
      if (ch === null || ch.length === 0) {
        return 0
      }

      const charCode = ch.charCodeAt(0)

      // eslint-disable-next-line prettier/prettier
      if (charCode <= 0x00007F) {
        return 1
        // eslint-disable-next-line prettier/prettier
      } else if (charCode <= 0x0007FF) {
        return 2
        // eslint-disable-next-line prettier/prettier
      } else if (charCode <= 0x00FFFF) {
        return 3
      } else {
        return 4
      }
    },
    unixTimeFilter(val) {
      const date = new Date(val + 1000)
        .toISOString()
        .slice(0, 19)
        .replace('T', ' ')
      return date.substring(0, 10)
    },

    /* 
    ================================================================================================
      백엔드로 데이터 전송
    ================================================================================================
    */
    testArr() {
      for (const i in this.angel.invArr) {
        console.log(this.angel.invArr[i])
      }
    },
    formCheck() {
      let res = false
      for (const f in this.form) {
        if (!this.form[f]) res = true
      }
      return res
    },
    submit() {
      const vm = this
      if (this.formCheck()) {
        // vm.requiredNotice = true
        setTimeout(function() {
          vm.requiredNotice = false
        }, 2000)
        return
      }
      this.submitProcess()
    },
    submitProcess() {
      this.$axios
        .post('/api/angel/register', JSON.stringify(this.angel))
        .then((res) => {
          this.pageToList(res.data.aSerial)
        })
        .catch((err) => {
          throw err
        })
    },
    async pageToList(hSerial) {
      this.complete = !this.complete
      await this.setStoreUserType()
      await this.setLocalStorage(hSerial)
      setTimeout(() => {
        this.complete = false
        this.$router.push({ path: '/angel/angelList' })
      }, 1500)
    },
    setLocalStorage(aSerial) {
      return new Promise((resolve, reject) => {
        const accountInfo = JSON.parse(localStorage.getItem('accountInfo'))
        accountInfo.accountCo = aSerial
        localStorage.setItem('accountInfo', JSON.stringify(accountInfo))
        resolve()
      })
    },
    setStoreUserType() {
      return new Promise((resolve, reject) => {
        this.$store.commit('userType/changeUserType', 'A01')
        resolve()
      })
    },
    setSample() {
      /*
        테스트 하기 위해 자동입력 샘플 내용
      */
      this.angel.regTel = '023503500'
      this.angel.regContPwd = 123123
      this.angel.coNameKor = '주식회사 엔젤테스트'
      this.angel.coNameEng = 'ANGEL TEST Co.Ltd'
      this.angel.representativeNameKor = '김엔젤'
      this.angel.representativeNameEng = 'Angel kim'
      this.angel.coTel = '025503030'
      this.angel.foundedDate = '2017-07-07'
      this.angel.coAddr = '서울시 동작구 상도동 엔젤테스트 주식회사'
      this.angel.coWeb = 'ange.co.kr'
      this.angel.coLogo = 'http://211.209.243.154:8082/angel_logo.png'

      this.angel.corpDiv = '01'
      this.angel.coStatus = '01'
      this.angel.largeField = '02'
      this.angel.smallField = '엔젤보드 주식회사 엔젤테스트 테스트 문구'
      this.angel.capital = '300,000,000,000'
      this.angel.invTypeL = '01'
      this.angel.invTypeS = '02'

      this.angel.hopCotype01 = '01'
      this.angel.hopCotype02 = '02'
      this.angel.hopCoSect01 = '01'
      this.angel.hopCoSect02 = '02'
      this.angel.hopCoItem =
        '엔젤보드 테스트의 선호하는 투자유치 기업의 유형 기술융합 투자 업체'
      this.angel.hopCoAddr01 = '03'
      this.angel.hopCoAddr02 = '02'
      this.angel.hopInvAmount = '02'
      this.angel.hopSalesVolume = '02'
      this.angel.hopOpProfit = '01'
      this.angel.etc = '주식회사 엔젤보드 테스트 회사 소개 테스트 문구'
    }
  }
}
</script>

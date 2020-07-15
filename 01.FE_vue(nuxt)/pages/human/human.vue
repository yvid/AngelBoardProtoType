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
          <span style="color: #BBDEFB; font-size:13px;">*표시: 필수입력</span>
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
                      ref="regEMailID"
                      v-model.lazy="human.regEMailID"
                      :rules="[() => !!human.regEMailID || '필수 입력!']"
                      :error-messages="errorMessages"
                      label="* 등록자 이메일"
                      placeholder="이메일 계정을 입력해주세요"
                      disabled
                      required
                      @blur="human.regEMailID = checkEmail($event.target.value)"
                    ></v-text-field>

                    <v-text-field
                      ref="regTel"
                      v-model="human.regTel"
                      :rules="[() => !!human.regTel || '필수 입력!']"
                      :error-messages="errorMessages"
                      label="* 등록자 연락처(숫자만 입력)"
                      placeholder="연락처를 입력해주세요"
                      required
                      @keyup="human.regTel = typingNum($event.target.value, 15)"
                    ></v-text-field>

                    <v-text-field
                      ref="regContPwd"
                      v-model="human.regContPwd"
                      :append-icon="show ? 'visibility' : 'visibility_off'"
                      :type="show ? 'text' : 'password'"
                      :rules="[() => !!human.regContPwd || '필수 입력!']"
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
                      v-model="human.coNameKor"
                      :rules="[() => !!human.coNameKor || '필수 입력!']"
                      :error-messages="errorMessages"
                      label="* 회사명(한글) - 주식회사의 경우 법인등기명칭으로 입력"
                      placeholder="한글 회사명을 입력해주세요"
                      required
                      @keyup="human.coNameKor = typingKor($event.target.value)"
                    ></v-text-field>

                    <v-text-field
                      ref="coNameEng"
                      v-model="human.coNameEng"
                      :rules="[() => !!human.coNameEng || '필수 입력!']"
                      :error-messages="errorMessages"
                      label="* 회사명(영문)"
                      placeholder="영문 회사명을 입력해주세요"
                      @keyup="human.coNameEng = typingEng($event.target.value)"
                    ></v-text-field>

                    <v-menu
                      ref="datePick01"
                      v-model="datePick01"
                      :close-on-content-click="false"
                      :return-value.sync="human.foundedDate"
                      transition="scale-transition"
                      offset-y
                      min-width="290px"
                    >
                      <template v-slot:activator="{ on }">
                        <v-text-field
                          v-model="human.foundedDate"
                          label="* 설립일: 선택"
                          prepend-icon="event"
                          readonly
                          v-on="on"
                        ></v-text-field>
                      </template>
                      <v-date-picker
                        v-model="human.foundedDate"
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
                          @click="$refs.datePick01.save(human.foundedDate)"
                          >선택</v-btn
                        >
                      </v-date-picker>
                    </v-menu>

                    <v-tooltip top>
                      <template v-slot:activator="{ on }">
                        <v-row class="d-flex align-baseline" no-gutters>
                          <v-col cols="4"><h4>* 회사 구분:</h4></v-col>
                          <v-col>
                            <v-select
                              ref="coDiv"
                              v-model="human.coDiv"
                              :rules="[() => !!human.coDiv || '필수 입력!']"
                              :items="coDivArr"
                              label="* 회사 구분"
                              placeholder="선택..(다중선택 가능)"
                              outlined
                              multiple
                              chips
                              required
                              v-on="on"
                            >
                            </v-select>
                          </v-col>
                        </v-row>
                      </template>
                      <span>닫기: 여백 클릭</span>
                    </v-tooltip>

                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* 법인 구분:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="corpDiv"
                          v-model="human.corpDiv"
                          :rules="[() => !!human.corpDiv || '필수 입력!']"
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
                          v-model="human.coStatus"
                          :rules="[() => !!human.coStatus || '필수 입력!']"
                          :items="coStatusArr"
                          label="* 회사 상태"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-chip-group>
                      <v-text-field
                        ref="coAddr"
                        v-model="human.coAddr"
                        :rules="[() => !!human.coAddr || '필수 입력!']"
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

                            <!-- <component
                              :is="currentComponents"
                              style="max-height: 600px; overflow: scroll;"
                              @complete="addrComplete"
                            /> -->
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
                      ref="coEmail"
                      v-model="human.coEmail"
                      :rules="[() => !!human.coEmail || '필수 입력!']"
                      :error-messages="errorMessages"
                      label="* 회사 이메일"
                      placeholder="회사 이메일 주소를 입력해주세요"
                      required
                      @blur="human.coEmail = checkEmail($event.target.value)"
                    ></v-text-field>

                    <v-text-field
                      ref="coWeb"
                      v-model="human.coWeb"
                      label="회사 웹사이트"
                      placeholder="회사 웹사이트 주소를 입력해주세요"
                    ></v-text-field>

                    <v-text-field
                      ref="coLogo"
                      v-model="human.coLogo"
                      label="회사로고 링크"
                      placeholder="회사로고 링크 주소를 입력해주세요"
                    ></v-text-field>

                    <v-text-field
                      ref="coTel"
                      v-model="human.coTel"
                      :rules="[() => !!human.coTel || '필수 입력!']"
                      :error-messages="errorMessages"
                      label="* 회사 연락처(숫자만 입력)"
                      required
                      placeholder="회사 연락처를 입력해주세요"
                      @keyup="human.coTel = typingNum($event.target.value, 15)"
                    ></v-text-field>
                  </v-card-text>
                </v-card>
              </v-tab-item>

              <!-- tab-2 start -->
              <v-tab-item>
                <v-card flat>
                  <v-card-text>
                    <v-text-field
                      ref="representativeNameKor"
                      v-model="human.representativeNameKor"
                      :rules="[
                        () => !!human.representativeNameKor || '필수 입력!'
                      ]"
                      :error-messages="errorMessages"
                      label="* 대표자명 - 한글"
                      placeholder="한글 대표자명을 입력해주세요"
                      required
                      @keyup="
                        human.representativeNameKor = typingKor(
                          $event.target.value
                        )
                      "
                    ></v-text-field>

                    <v-text-field
                      ref="representativeNameEng"
                      v-model="human.representativeNameEng"
                      :rules="[
                        () => !!human.representativeNameEng || '필수 입력!'
                      ]"
                      :error-messages="errorMessages"
                      label="* 대표자명 - 영문"
                      placeholder="영문 대표자명을 입력해주세요"
                      required
                      @keyup="
                        human.representativeNameEng = typingEng(
                          $event.target.value
                        )
                      "
                    ></v-text-field>

                    <v-text-field
                      ref="representativeTel"
                      v-model="human.representativeTel"
                      :rules="[() => !!human.representativeTel || '필수 입력!']"
                      :error-messages="errorMessages"
                      label="* 대표자 연락처(숫자만 입력)"
                      placeholder="연락처를 입력 해주세요"
                      required
                      @keyup="
                        human.representativeTel = typingNum(
                          $event.target.value,
                          15
                        )
                      "
                    ></v-text-field>

                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* 대표자 국적:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="representativeNationality"
                          v-model="human.representativeNationality"
                          :rules="[
                            () =>
                              !!human.representativeNationality || '필수 입력!'
                          ]"
                          :error-messages="errorMessages"
                          :items="countries"
                          label="* 대표자 국적"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* 대표자 성별:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="representativeGender"
                          v-model="human.representativeGender"
                          :rules="[
                            () => !!human.representativeGender || '필수 입력!'
                          ]"
                          :error-messages="errorMessages"
                          :items="genOpt"
                          label="* 대표자 성별"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"
                        ><h4>* 대표자, 설립자 동일 확인:</h4></v-col
                      >
                      <v-col
                        ><v-select
                          ref="representativeFounderSame"
                          v-model="human.representativeFounderSame"
                          :rules="[
                            () =>
                              !!human.representativeFounderSame || '필수 입력!'
                          ]"
                          :error-messages="errorMessages"
                          :items="representativeFounderSameArr"
                          label="* 대표자 / 설립자 동일 유무"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <div
                      v-show="
                        human.representativeFounderSame !== null &&
                          human.representativeFounderSame === '02'
                      "
                    >
                      <v-text-field
                        ref="founderNameKor"
                        v-model="human.founderNameKor"
                        :rules="[() => !!human.founderNameKor || '필수 입력!']"
                        :error-messages="errorMessages"
                        label="* 설립자명"
                        placeholder="설립자명을 입력해주세요"
                        required
                      ></v-text-field>
                    </div>

                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* 공동대표자 유무:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="coRepresentative"
                          v-model="human.coRepresentative"
                          :rules="[
                            () => !!human.coRepresentative || '필수 입력!'
                          ]"
                          :error-messages="errorMessages"
                          :items="coRepresentativeArr"
                          label="* 공동대표자 유무"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <div
                      v-show="
                        human.coRepresentative !== null &&
                          human.coRepresentative === '01'
                      "
                    >
                      <v-text-field
                        ref="coRepresentativeNameKor"
                        v-model="human.coRepresentativeNameKor"
                        :rules="[
                          () => !!human.coRepresentativeNameKor || '필수 입력!'
                        ]"
                        :error-messages="errorMessages"
                        label="* 공동대표자명"
                        placeholder="공동대표자명을 입력해주세요"
                        required
                      ></v-text-field>
                    </div>
                  </v-card-text>
                </v-card>
              </v-tab-item>

              <!-- tab-3 start -->
              <v-tab-item>
                <v-card flat>
                  <v-card-text>
                    <v-text-field
                      ref="serviceNameKor"
                      v-model="human.serviceNameKor"
                      :rules="[() => !!human.serviceNameKor || '필수 입력!']"
                      :error-messages="errorMessages"
                      label="* 서비스명 - 한글"
                      placeholder="예시)  종목명이 아닌 브랜드명"
                      required
                      @keyup="
                        human.serviceNameKor = typingKor($event.target.value)
                      "
                    ></v-text-field>

                    <v-text-field
                      ref="serviceNameEng"
                      v-model="human.serviceNameEng"
                      label="서비스명 - 영문"
                      placeholder="영문 서비스명을 입력해주세요"
                      required
                      @keyup="
                        human.serviceNameEng = typingEng($event.target.value)
                      "
                    ></v-text-field>

                    <v-textarea
                      ref="serviceSummary"
                      v-model="human.serviceSummary"
                      outlined
                      :rules="[() => !!human.serviceSummary || '필수 입력!']"
                      success-messages="직접입력"
                      :error-messages="errorMessages"
                      :label="
                        '* 서비스 설명(요약 ' +
                          countByte(human.serviceSummary, 500)
                      "
                      placeholder="서비스 설명을 입력해주세요"
                      rows="2"
                      auto-grow
                      required
                      @keyup="
                        human.serviceSummary = chkByte(
                          human.serviceSummary,
                          500
                        )
                      "
                    ></v-textarea>

                    <v-textarea
                      ref="patent"
                      v-model="human.patent"
                      outlined
                      success-messages="직접입력"
                      :label="
                        '특허 관련 - 키프리스 확인 가능한 내용을 포함하여 입력 (' +
                          countByte(human.patent, 500)
                      "
                      placeholder="특허(국내, 해외) / 상표권 / 실용신안등의 관련 보유 등록번호 및 내용을 입력해주세요"
                      rows="2"
                      auto-grow
                      @keyup="human.patent = chkByte(human.patent, 500)"
                    ></v-textarea>

                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* 기술:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="tech"
                          v-model="human.tech"
                          :rules="[() => !!human.tech || '필수 입력!']"
                          :error-messages="errorMessages"
                          :items="tech"
                          label="* 기술"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* 대분야:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="largeField"
                          v-model="human.largeField"
                          :rules="[() => !!human.largeField || '필수 입력!']"
                          :error-messages="errorMessages"
                          :items="largeField"
                          label="* 대분야"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-text-field
                      ref="smallField"
                      v-model="human.smallField"
                      :rules="[() => !!human.smallField || '필수 입력!']"
                      :error-messages="errorMessages"
                      label="* 소분야 - 세부분야명"
                      required
                      placeholder="예시)  대분야: '생활' / 소분야: '재사용 마스크'"
                    ></v-text-field>

                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* o2o:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="coRepresentative"
                          v-model="human.o2o"
                          :rules="[() => !!human.o2o || '필수 입력!']"
                          :error-messages="errorMessages"
                          :items="o2o"
                          label="* O2O (Online To Offline)"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-spacer></v-spacer>
                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* 사업 형태:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="businessType"
                          v-model="human.businessType"
                          :rules="[() => !!human.businessType || '필수 입력!']"
                          :error-messages="errorMessages"
                          :items="businessType"
                          label="* 사업 형태"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* 서비스 형태:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="serviceType"
                          v-model="human.serviceType"
                          :rules="[() => !!human.serviceType || '필수 입력!']"
                          :error-messages="errorMessages"
                          :items="serviceType"
                          label="* 서비스 형태"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* 서비스 상태:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="serviceStatus"
                          v-model="human.serviceStatus"
                          :rules="[() => !!human.serviceStatus || '필수 입력!']"
                          :error-messages="errorMessages"
                          :items="serviceStatus"
                          label="* 서비스 상태"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-text-field
                      ref="serviceURL"
                      v-model="human.serviceURL"
                      label="서비스 링크"
                      placeholder="서비스 웹사이트 또는 소개자료 링크를 입력해주세요"
                    ></v-text-field>

                    <v-textarea
                      ref="similarService"
                      v-model="human.similarService"
                      outlined
                      success-messages="직접입력"
                      :label="
                        '유사서비스 (' + countByte(human.similarService, 400)
                      "
                      placeholder="기존에 있는 유사서비스 내용을 입력해주세요(있을 경우 입력)"
                      rows="2"
                      auto-grow
                      @keyup="
                        human.similarService = chkByte(
                          human.similarService,
                          400
                        )
                      "
                    ></v-textarea>

                    <v-text-field
                      ref="serviceLogo"
                      v-model="human.serviceLogo"
                      label="서비스로고 링크"
                      placeholder="서비스로고 링크 주소를 입력해주세요"
                    ></v-text-field>
                  </v-card-text>
                </v-card>
              </v-tab-item>
              <!-- tab-4 start -->
              <v-tab-item>
                <v-card flat>
                  <v-card-text>
                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* 현재 투자단계:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="invStage"
                          v-model="human.invStage"
                          :rules="[() => !!human.invStage || '필수 입력!']"
                          :error-messages="errorMessages"
                          :items="invStage"
                          label="* 현재 투자단계"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* 전년도 매출규모:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="prevYearSaleVolume"
                          v-model="human.prevYearSaleVolume"
                          :rules="[
                            () => !!human.prevYearSaleVolume || '필수 입력!'
                          ]"
                          :error-messages="errorMessages"
                          :items="prevYearSaleVolume"
                          label="* 전년도 매출규모"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-text-field
                      ref="invAttrTargetAmount"
                      v-model="human.invAttrTargetAmount"
                      :rules="[
                        () => !!human.invAttrTargetAmount || '필수 입력!'
                      ]"
                      :error-messages="errorMessages"
                      label="* 현재 투자유치 목표금액(억) 숫자만 입력"
                      required
                      placeholder="예시)  1억을 경우 1 을 입력"
                      suffix="억원"
                      type="number"
                    ></v-text-field>

                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>* 투자금 사용목적:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="invFundPurpose"
                          v-model="human.invFundPurpose"
                          :rules="[
                            () => !!human.invFundPurpose || '필수 입력!'
                          ]"
                          :error-messages="errorMessages"
                          :items="invFundPurpose"
                          label="* 투자금 사용 목적"
                          placeholder="선택..(다중선택 가능)"
                          outlined
                          chips
                          multiple
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-textarea
                      ref="problemsToSolve"
                      v-model="human.problemsToSolve"
                      :error-messages="errorMessages"
                      outlined
                      success-messages="직접입력"
                      :label="
                        '* 서비스(아이템)관련 해결하고자 하는 문제 (' +
                          countByte(human.problemsToSolve, 500)
                      "
                      placeholder="서비스 관련하여 해결하고자 하는 문제 내용을 입력해주세요"
                      rows="2"
                      auto-grow
                      required
                      @keyup="
                        human.problemsToSolve = chkByte(
                          human.problemsToSolve,
                          500
                        )
                      "
                    ></v-textarea>

                    <v-textarea
                      ref="ourSolution"
                      v-model="human.ourSolution"
                      :error-messages="errorMessages"
                      outlined
                      success-messages="직접입력"
                      :label="
                        '* 서비스(아이템)관련 문제해결을 위한 해결책 (' +
                          countByte(human.ourSolution, 500)
                      "
                      placeholder="서비스 관련 문제 해결을 위한 해결책 내용을 입력해주세요"
                      rows="2"
                      auto-grow
                      required
                      @keyup="
                        human.ourSolution = chkByte(human.ourSolution, 500)
                      "
                    ></v-textarea>

                    <v-textarea
                      ref="aboutTeam"
                      v-model="human.aboutTeam"
                      :error-messages="errorMessages"
                      outlined
                      success-messages="직접입력"
                      :label="
                        '* 서비스(아이템)구성원 - 경력 / 자원 관련하여 서술 (' +
                          countByte(human.aboutTeam, 500)
                      "
                      placeholder="서비스 관련 구성원에 대한 내용을 입력해주세요"
                      rows="2"
                      auto-grow
                      required
                      @keyup="human.aboutTeam = chkByte(human.aboutTeam, 500)"
                    ></v-textarea>

                    <v-text-field
                      ref="capital"
                      v-model="human.capital"
                      :rules="[() => !!human.capital || '필수 입력!']"
                      :error-messages="errorMessages"
                      label="* 자본금 (숫자만 입력)"
                      required
                      placeholder="금액을 숫자만 입력해주세요"
                      @keyup="
                        human.capital = typingCash($event.target.value, 50)
                      "
                    ></v-text-field>

                    <v-text-field
                      ref="totalAssets"
                      v-model="human.totalAssets"
                      :rules="[() => !!human.totalAssets || '필수 입력!']"
                      :error-messages="errorMessages"
                      label="* 총자산합계 (숫자만 입력)"
                      required
                      placeholder="금액을 숫자만 입력해주세요"
                      @keyup="
                        human.totalAssets = typingCash($event.target.value, 50)
                      "
                    ></v-text-field>

                    <v-text-field
                      ref="totalLiabilities"
                      v-model="human.totalLiabilities"
                      :rules="[() => !!human.totalLiabilities || '필수 입력!']"
                      :error-messages="errorMessages"
                      label="* 총부채 (숫자만 입력)"
                      required
                      placeholder="금액을 숫자만 입력해주세요"
                      @keyup="
                        human.totalLiabilities = typingCash(
                          $event.target.value,
                          50
                        )
                      "
                    ></v-text-field>

                    <v-text-field
                      ref="numberOfEmp"
                      v-model="human.numberOfEmp"
                      :rules="[() => !!human.numberOfEmp || '필수 입력!']"
                      :error-messages="errorMessages"
                      label="* 종업원수 (숫자만 입력)"
                      required
                      placeholder="예시)  2명일 경우: 2, 1인기업의 경우: 1"
                      @keyup="
                        human.numberOfEmp = typingNum($event.target.value, 50)
                      "
                    ></v-text-field>
                  </v-card-text>
                </v-card>
              </v-tab-item>
              <!-- tab-5 start -->
              <v-tab-item>
                <v-card flat>
                  <v-card-text>
                    <v-row class="d-flex align-baseline" no-gutters>
                      <v-col cols="4"><h4>투자유치실적 정보 유무:</h4></v-col>
                      <v-col
                        ><v-select
                          ref="invInfo"
                          v-model="human.invInfo"
                          :rules="[() => !!human.invInfo || '필수 입력!']"
                          :error-messages="errorMessages"
                          :items="invInfo"
                          label="* 투자유치실적 정보 유무"
                          placeholder="선택.."
                          outlined
                          required
                        ></v-select
                      ></v-col>
                    </v-row>

                    <v-switch
                      v-if="human.invInfo === '01'"
                      v-model="human.invInfoAddIntention"
                      :label="
                        `투자유치실적 정보'를 공개 하시겠습니까? ${invInfoAddIntentionVal}`
                      "
                    ></v-switch>
                    <div v-if="human.invInfo === '01'">
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
                        <span style="font-size: 16px;"
                          >투자유치실적 이력 수</span
                        >
                      </div>

                      <div v-for="(item, i) in invTime" :key="i">
                        <v-divider />
                        <div style="margin-bottom:20px; margin-top:20px;">
                          <v-chip> # 투자유치실적 이력: {{ item }}</v-chip>
                        </div>

                        <v-menu
                          ref="datePick02"
                          v-model="human.invArr[i].datePick02"
                          :close-on-content-click="false"
                          :return-value.sync="human.invArr[i].preInvDate"
                          transition="scale-transition"
                          offset-y
                          min-width="290px"
                        >
                          <template v-slot:activator="{ on }">
                            <v-text-field
                              v-model="human.invArr[i].preInvDate"
                              label="* 투자유치날짜: 선택"
                              prepend-icon="event"
                              readonly
                              v-on="on"
                            ></v-text-field>
                          </template>
                          <v-date-picker
                            v-model="human.invArr[i].preInvDate"
                            no-title
                            scrollable
                          >
                            <v-spacer></v-spacer>
                            <v-btn
                              text
                              color="primary"
                              @click="human.invArr[i].datePick02 = false"
                              >취소</v-btn
                            >
                            <v-btn
                              text
                              color="primary"
                              @click="
                                $refs.datePick02[i].save(
                                  human.invArr[i].preInvDate
                                )
                              "
                              >선택</v-btn
                            >
                          </v-date-picker>
                        </v-menu>

                        <v-row class="d-flex align-baseline" no-gutters>
                          <v-col cols="4"><h4>* 투자유치 단계:</h4></v-col>
                          <v-col
                            ><v-select
                              ref="preInvStage"
                              v-model="human.invArr[i].preInvStage"
                              :rules="[
                                () =>
                                  !!human.invArr[i].preInvStage || '필수 입력!'
                              ]"
                              :error-messages="errorMessages"
                              :items="preInvStage"
                              label="* 투자유치 단계"
                              placeholder="선택.."
                              outlined
                              required
                            ></v-select
                          ></v-col>
                        </v-row>

                        <v-text-field
                          ref="totalInvAmount"
                          v-model="human.invArr[i].preInvAmount"
                          :rules="[
                            () => !!human.invArr[i].preInvAmount || '필수 입력!'
                          ]"
                          :error-messages="errorMessages"
                          label="* 투자받은금액(억)"
                          required
                          placeholder="억원"
                          suffix="억원"
                          type="number"
                        ></v-text-field>

                        <v-text-field
                          ref="preInvestor"
                          v-model="human.invArr[i].preInvestor"
                          :rules="[
                            () => !!human.invArr[i].preInvestor || '필수 입력!'
                          ]"
                          :error-messages="errorMessages"
                          label="* 투자자 (직업입력)"
                          required
                          placeholder="투자자(기업, 기관, 개인) 정보를 입력해주세요"
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
              <v-btn class="ma-2" tile outlined color="gray" @click="submit">
                <v-icon>mdi-domain</v-icon> 등록
              </v-btn>
            </v-col>
            <v-col>
              <v-btn
                v-if="tabs < 4"
                class="ma-2"
                tile
                outlined
                color="success"
                @click="nextTab"
              >
                <v-icon left>mdi-pencil</v-icon> 다음
              </v-btn>
            </v-col>
            <!-- 
            <v-col>
              <v-btn @click="testStore()">다이얼로그 </v-btn>
            </v-col>
             -->
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

    <v-dialog v-model="invComplete" max-width="400">
      <v-card>
        <v-card-title>
          <span>투자 실적 정보를 모두 입력해주세요.</span>
          <v-spacer></v-spacer>
        </v-card-title>
        <v-card-actions class="d-flex flex-row-reverse">
          <v-btn color="primary" text @click="complete = false">
            닫기
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
    currentComponents: null,
    countries: [],
    tabs: null,
    items: [
      { id: 1, name: '기업 기본 정보' },
      { id: 2, name: '기업 대표자 정보' },
      { id: 3, name: '기업 아이템 정보' },
      { id: 4, name: '기업 상태 정보' },
      { id: 5, name: '기업 투자 정보' }
    ],
    text: 'consequat.',
    errorMessages: '',
    show: false,
    dialog: false,
    complete: false,
    invComplete: false,
    requiredNotice: false,
    human: {
      hSerial: null,

      /* tab-1 */
      regEMailID: null,
      regTel: null,
      regContPwd: null,
      coNameKor: null,
      coNameEng: null,
      foundedDate: new Date().toISOString().substr(0, 10),
      coDiv: null,
      corpDiv: null,
      coStatus: null,
      coAddr: null,
      coEmail: null,
      coWeb: null,
      coLogo: null,
      coTel: null,

      /* tab-2 */
      representativeNameKor: null,
      representativeNameEng: null,
      representativeTel: null,
      representativeNationality: null,
      representativeGender: null,
      representativeFounderSame: { text: '동일', value: '01' },
      founderNameKor: null,
      coRepresentative: { text: '무', value: '02' },
      coRepresentativeNameKor: null,

      /* tab-3 */
      serviceNameKor: null,
      serviceNameEng: null,
      serviceSummary: null,
      patent: null,
      tech: null,
      largeField: null,
      smallField: null,
      o2o: null,
      businessType: null,
      serviceType: null,
      serviceStatus: null,
      serviceURL: null,
      similarService: null,
      serviceLogo: null,

      /* tab-4 */
      invStage: null,
      prevYearSaleVolume: null,
      invAttrTargetAmount: null,
      invFundPurpose: null,
      problemsToSolve: null,
      ourSolution: null,
      aboutTeam: null,
      capital: null,
      totalAssets: null,
      totalLiabilities: null,
      numberOfEmp: null,

      /* tab-5 */
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
    invInfoAddIntentionMsg: '네',
    genOpt: [
      { text: '남', value: '01' },
      { text: '여', value: '02' }
    ],
    coDivArr: [],
    corpDivArr: [],
    coStatusArr: [],
    representativeFounderSameArr: [],
    coRepresentativeArr: [],
    tech: [],
    largeField: [],
    o2o: [],
    businessType: [],
    serviceType: [],
    serviceStatus: [],
    invStage: [],
    prevYearSaleVolume: [],
    invFundPurpose: [],
    invInfo: [],
    invInfoAddIntention: [],
    preInvStage: []
  }),
  computed: {
    form() {
      return {
        /* tab-1 */
        regEMailID: this.human.regEMailID,
        regTel: this.human.regTel,
        regContPwd: this.human.regContPwd,
        coNameKor: this.human.coNameKor,
        coNameEng: this.human.coNameEng,
        foundedDate: this.human.foundedDate,
        coDiv: this.human.coDiv,
        corpDiv: this.human.corpDiv,
        coStatus: this.human.coStatus,
        coAddr: this.human.coAddr,
        coEmail: this.human.coEmail,
        coTel: this.human.coTel,

        /* tab-2 */
        representativeNameKor: this.human.representativeNameKor,
        representativeNameEng: this.human.representativeNameEng,
        representativeTel: this.human.representativeTel,
        representativeNationality: this.human.representativeNationality,
        representativeGender: this.human.representativeGender,
        representativeFounderSame: this.human.representativeFounderSame,
        coRepresentative: this.human.coRepresentative,

        /* tab-3 */
        serviceNameKor: this.human.serviceNameKor,
        serviceNameEng: this.human.serviceNameEng,
        serviceSummary: this.human.serviceSummary,
        tech: this.human.tech,
        largeField: this.human.largeField,
        smallField: this.human.smallField,
        o2o: this.human.o2o,
        businessType: this.human.businessType,
        serviceType: this.human.serviceType,
        serviceStatus: this.human.serviceStatus,

        /* tab-4 */
        invStage: this.human.invStage,
        prevYearSaleVolume: this.human.prevYearSaleVolume,
        invAttrTargetAmount: this.human.invAttrTargetAmount,
        invFundPurpose: this.human.invFundPurpose,
        problemsToSolve: this.human.problemsToSolve,
        ourSolution: this.human.ourSolution,
        aboutTeam: this.human.aboutTeam,
        capital: this.human.capital,
        totalAssets: this.human.totalAssets,
        totalLiabilities: this.human.totalLiabilities,
        numberOfEmp: this.human.numberOfEmp,

        /* tab-5 */
        invInfo: this.human.invInfo
      }
    },
    invInfoAddIntentionVal() {
      return this.human.invInfoAddIntention ? '네' : '아니오'
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
    this.coDivArr = category.coDivArr
    this.corpDivArr = category.corpDivArr
    this.coStatusArr = category.coStatusArr
    this.representativeFounderSameArr = category.representativeFounderSameArr
    this.coRepresentativeArr = category.coRepresentativeArr
    this.tech = category.tech
    this.largeField = category.largeField
    this.o2o = category.o2o
    this.businessType = category.businessType
    this.serviceType = category.serviceType
    this.serviceStatus = category.serviceStatus
    this.invStage = category.invStage
    this.prevYearSaleVolume = category.prevYearSaleVolume
    this.invFundPurpose = category.invFundPurpose
    this.invInfo = category.invInfo
    this.invInfoAddIntention = category.invInfoAddIntention
    this.preInvStage = category.preInvStage
  },

  mounted() {
    if (localStorage.getItem('account') !== null)
      this.human.regEMailID = localStorage.getItem('account')
    this.getAccountCompSerial(JSON.parse(localStorage.getItem('accountInfo')))
  },
  methods: {
    getAccountCompSerial(accountInfo) {
      if (accountInfo.accountCo !== '' && accountInfo.accountCo !== null) {
        this.modify = true
        this.$axios
          .post(
            '/api/human/detail',
            JSON.stringify({ hSerial: accountInfo.accountCo })
          )
          .then((res) => {
            this.human = res.data[0][0]
            this.human.invArr = [
              {
                datePick02: false,
                preInvDate: new Date().toISOString().substr(0, 10),
                preInvTime: 1,
                preInvStage: null,
                preInvAmount: null,
                preInvestor: null
              }
            ]
            /* 대표자/설립자/공동대표 설정 */
            if (res.data[0][0].representativeFounderSame === '01') {
              this.human.representativeFounderSame = {
                text: '동일',
                value: '01'
              }
            } else {
              this.human.representativeFounderSame = {
                text: '비동일',
                value: '02'
              }
            }

            if (res.data[0][0].coRepresentative === '01') {
              this.human.coRepresentative = { text: '유', value: '01' }
            } else {
              this.human.coRepresentative = { text: '무', value: '02' }
            }

            /* coDiv(회사구분) 다중선택 수정 시 기존값 적용 */
            this.human.coDiv = []
            for (const i in res.data[1]) {
              this.human.coDiv[i] = res.data[1][i].coDiv
            }

            this.human.foundedDate = this.unixTimeFilter(this.human.foundedDate)
            this.human.capital = this.typingCash(
              this.human.capital.toString(),
              50
            )
            this.human.totalAssets = this.typingCash(
              this.human.totalAssets.toString(),
              50
            )
            this.human.totalLiabilities = this.typingCash(
              this.human.totalLiabilities.toString(),
              50
            )

            /* invFundPurpose(투자금 사용목적) 다중선택 수정 시 기존값 적용 */
            this.human.invFundPurpose = []
            for (const i in res.data[2]) {
              this.human.invFundPurpose[i] = res.data[2][i].invFundPurpose
            }

            if (res.data[3].length > 0) {
              this.invTime = res.data[3].length
              /* invArr(투자실적 정보) 다중선택 수정 시 기존값 적용 */
              for (const i in res.data[3]) {
                this.human.invArr[i] = res.data[3][i]
                this.human.invArr[i].preInvDate = this.unixTimeFilter(
                  this.human.invArr[i].preInvDate
                )
              }
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
      this.human.coAddr = res.address
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
    typingCash(e, byte) {
      const pattern = /[^0-9]/

      let res = this.chkByte(e).replace(pattern, '')
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
      this.human.invArr.splice(this.invTime - 1)
      this.invTime--
    },
    invTimePlus() {
      this.human.invArr[this.invTime] = {
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
      for (const i in this.human.invArr) {
        console.log(this.human.invArr[i])
      }
    },
    formCheck() {
      let res = false
      for (const f in this.form) {
        if (!this.form[f]) res = true
      }
      return res
    },
    preInvformCheck() {
      if (this.human.invInfo === '01') {
        const invArr = this.human.invArr
        for (const i in invArr) {
          if (invArr[i].preInvStage === null || invArr[i].preInvStage === '') {
            this.preInvDialogOn()
            return
          }
          if (
            invArr[i].preInvAmount === null ||
            invArr[i].preInvAmount === ''
          ) {
            this.preInvDialogOn()
            return
          }
          if (invArr[i].preInvestor === null || invArr[i].preInvestor === '') {
            this.preInvDialogOn()
            return
          }
        }
      }
    },
    preInvDialogOn() {
      this.invComplete = !this.invComplete
      setTimeout(function() {
        this.invComplete = !this.invComplete
      }, 2000)
    },
    submit() {
      const vm = this
      if (this.formCheck()) {
        vm.requiredNotice = true
        setTimeout(function() {
          vm.requiredNotice = false
        }, 2000)
        return
      }
      this.submintProcess()
    },
    submintProcess() {
      this.$axios
        .post('/api/human/register', JSON.stringify(this.human))
        .then((res) => {
          this.pageToList(res.data.hSerial)
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
        this.$router.push({ path: '/human/humanList' })
      }, 1500)
    },
    setLocalStorage(hSerial) {
      return new Promise((resolve, reject) => {
        const accountInfo = JSON.parse(localStorage.getItem('accountInfo'))
        accountInfo.accountCo = hSerial
        localStorage.setItem('accountInfo', JSON.stringify(accountInfo))
        resolve()
      })
    },
    setStoreUserType() {
      return new Promise((resolve, reject) => {
        this.$store.commit('userType/changeUserType', 'H01')
        resolve()
      })
    },
    movePageToAngelList() {
      this.$router.push({ path: '/human/humanList' })
    },
    testStore() {
      this.$store.commit('userType/changeUserType', 'H01')
    },
    setSample() {
      /*
        테스트 하기 위해 자동입력 샘플 내용
      */
      this.human.regTel = '01055002200'
      this.human.regContPwd = 123123
      this.human.coNameEng = 'TEST Co, LTD'
      this.human.coDiv = ['01', '02']
      this.human.corpDiv = '01'
      this.human.coStatus = '01'
      this.human.coAddr = '서울 동작구 상도동 엔젤보드 주식회사'
      this.human.coNameKor = '주식회사 테스트'
      this.human.coEmail = 'smaple@mail.com'
      this.human.coWeb = 'acmd.co.kr'
      this.human.coLogo = 'http://211.209.243.154:8082/angel_logo.png'
      this.human.coTel = '025506565'

      this.human.representativeNameKor = '김사장'
      this.human.representativeNameEng = 'Boss Kim'
      this.human.representativeTel = '01021213232'
      this.human.representativeNationality = 'South Korea'
      this.human.representativeGender = '01'
      this.human.representativeFounderSame = { text: '동일', value: '01' }
      this.human.coRepresentative = { text: '유', value: '01' }
      this.human.coRepresentativeNameKor = '임사장'

      this.human.serviceNameKor = '엔젤보드 투자 유치사 서비스명'
      this.human.serviceNameEng = 'Angel Board Human Serivce Name'
      this.human.serviceSummary = '엔젤보드 투자 유치사 서비스 요약 내용'
      this.human.patent = '특허: 국내 001/ 해외 002'
      this.human.tech = '03'
      this.human.largeField = '03'
      this.human.smallField = '엔젤보드 투자 유치사 서비스 소분야 내용'
      this.human.o2o = '01'
      this.human.businessType = '02'
      this.human.serviceType = '02'
      this.human.serviceStatus = '01'
      this.human.serviceURL = 'acmd.co.kr'
      this.human.similarService =
        '엔젤보드와 유사한 서비스는 투자서비스는 있지만 기술융합 서비스는 없습니다.'
      this.human.serviceLogo = 'http://211.209.243.154:8082/angel_logo.png'

      this.human.invStage = '01'
      this.human.prevYearSaleVolume = '01'
      this.human.invAttrTargetAmount = 3
      this.human.invFundPurpose = ['01', '03']
      this.human.problemsToSolve =
        '엔젤보드의 해결할 문제는 엔젤보드 서비스 인프라 입니다.'
      this.human.ourSolution =
        '엔젤보드 서비스 인프라를 위해 투자유치 중 입니다.'
      this.human.aboutTeam =
        '엔젤보드와 에이씨엠디 멤버는 대표, 이사, 실장, 팀장'
      this.human.capital = '50,000,000'
      this.human.totalAssets = '150,000,000'
      this.human.totalLiabilities = '30,000,000'
      this.human.numberOfEmp = 25
    }
  }
}
</script>

<style>
.complete {
  position: absolute;
  top: 30%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>

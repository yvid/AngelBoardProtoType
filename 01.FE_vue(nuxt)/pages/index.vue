<template>
  <v-layout column justify-center align-center>
    <v-flex xs12 sm8 md6>
      <div class="text-center">
        <img src="/angel_logo.png" alt="Vuetify.js" class="mb-5" />
      </div>
      <div v-if="false">
        <v-card-title>
          <v-text-field
            v-model="search"
            append-icon="search"
            label="업체명 입력..."
            single-line
            hide-details
          ></v-text-field> </v-card-title
        ><v-card-title>
          <v-select
            v-model="enabled"
            :items="slots"
            label="분야별 선택..."
            clearable
          ></v-select>
        </v-card-title>
      </div>
      <small>
        <em>
          유망 기술 기업간 협력관계 구축 및 투자유치 플랫폼 입니다.<br /><br />

          1. 사업개요<br />
          새로운 이이템(아이디어) 또는 신기술을 가진 유망 기술기업들과 투자자가
          <br />
          서로 참여하여 투자 유치 및 기술융합 컨소시엄 결합이 가능한 플랫폼<br />
          <br />
          2. 엔젤보드 프로세스<br />
          엔젤보드 플랫폼에 등록 된 사업체와 투자자의 정보를 상호간
          커뮤니케이션이 가능하게 지원<br />
          유망 기술 기업간 협력체계 구축 및 투자 연계와 디딤돌의 역할 수행,
          공동사업모델 도출<br /><br />
          &mdash;주식회사 에이씨엠디 - 숨 -&mdash;
        </em>
      </small>
    </v-flex>
  </v-layout>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import Logo from '~/components/Logo.vue'
// eslint-disable-next-line no-unused-vars
import VuetifyLogo from '~/components/VuetifyLogo.vue'

export default {
  components: {},
  data() {
    return {
      search: '',
      enabled: null,
      slots: [
        '홈',
        '생활',
        '전자제품',
        '음식',
        '쇼핑',
        '물류 / 유통',
        '유아',
        '애완동물',
        '스포츠',
        '패션',
        '뷰티',
        '게임',
        '여행',
        '교육',
        '모임 / 행사',
        '사회 / 봉사',
        '바이오 / 의료',
        '헬스케어',
        '기업',
        '광고마케팅',
        '금융',
        '보안',
        '블록체인',
        '엔터테인먼트',
        '콘텐츠',
        'VR / AR',
        '3D 프린터',
        '항공기 / 드론',
        '환경 / 에너지',
        '자전거',
        '오토바이',
        '자동차',
        '선박',
        '건설',
        '부동산',
        '축산업',
        '농산업',
        '수산업',
        '방송 / 언론',
        '화학',
        '군수',
        '우주 / 항공'
      ]
    }
  }
}
</script>

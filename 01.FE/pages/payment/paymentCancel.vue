<template>
  <body>
    <p>결제가 취소 되었습니다.</p>
  </body>
</template>

<script>
export default {
  mounted() {
    this.init()
  },
  methods: {
    init() {
      window.close()
    }
  }
}
</script>

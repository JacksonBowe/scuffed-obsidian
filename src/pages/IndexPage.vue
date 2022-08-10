<template>
  <q-page class="" dark>

    <!-- <div> -->

    <q-markdown :src="content" class="q-pl-lg" :key="content" />

    <!-- </div> -->
  </q-page>
</template>

<script>
import { defineComponent, computed, onUpdated, onMounted, ref } from 'vue'
import { useQuasar } from 'quasar'
// import markdown from "../content/Note B.md"

import { onBeforeRouteUpdate, useRoute } from 'vue-router'

export default defineComponent({
  name: 'IndexPage',
  setup () {

    const route = useRoute()


    onMounted(async () => {
      await loadContent()
    })

    onUpdated(async () => {
      await loadContent()
    })

    const content = ref(null)

    const loadContent = async () => {
      const route = useRoute()
      console.log('updated, using '+ `..${route.path}`)
      let markdown = await import(`..${route.path}`)
      content.value = markdown.default
    }


    // onBeforeRouteUpdate(async (to, from, next) => {
    //   markdown = await import(`..${to.path}`)
    //   console.log(`..${to.path}`)
    //   console.log(markdown)
    //   console.log(to, from)
    //   next()
    // })

    const q = useQuasar()


    q.dark.set(true)

    return {
      content
    }
  }
})
</script>

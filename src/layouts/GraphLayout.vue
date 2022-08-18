<template>
  <q-layout view="hHh LpR lFf" dark class="">

    <s-toolbar />
        
    <q-page-container>
        <router-view />
    </q-page-container>


  </q-layout>
</template>

<script>
import { defineComponent } from 'vue'
import SToolbar from 'src/components/ScuffedToolbar.vue'




export default defineComponent({
    name: 'ContentLayout',

    components: {
        SToolbar
    },

    setup () {

        const openGraph = () => {
            // TODO
            console.log('opening graph')
        }

        return {
            openGraph,
        }
    }
})
</script>

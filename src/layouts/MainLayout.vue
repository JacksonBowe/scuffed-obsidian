<template>
  <q-layout view="hHh LpR lFf" class="">
    <q-header elevated dark class="bg-transparent">
      <q-toolbar class="row bg-transparent" dark>
        <div class="col-2" style="max-width:200px"></div>
        <div class="row col q-mr-md">
            <q-btn
              flat
              dense
              round
              icon="menu"
              aria-label="Menu"
              @click="toggleLeftDrawer"
            />

            <q-toolbar-title class="content-center flex">
            Quasar App
            </q-toolbar-title>
            <q-input  rounded dense dark standout />

        </div>
        
        <div>
            Quasar v{{ $q.version }}
        </div>
      </q-toolbar>
    </q-header>

      <div class="row">
        <div class="col-2" style="max-width: 200px"></div>
        <div class="col-2 q-pt-xl">
            <q-list class="q-pt-lg"  dense >
                <q-item-label class="text-secondary text-overline" header>
                	Docs
                </q-item-label>
                <custom-list v-for="child in contentItems.children" :key="child" :item="child" />
            </q-list>
        </div>
        <q-page-container class="col">
            <router-view />
        </q-page-container>
      </div>

    <!-- </div> -->


  </q-layout>
</template>

<script>
import { defineComponent, ref } from 'vue'
// import EssentialLink from 'components/EssentialLink.vue'
import CustomList from 'src/components/CustomList.vue'
import contentItems from '../content/.map.json'

const linksList = [
  {
    title: 'Docs',
    caption: 'quasar.dev',
    icon: 'school',
    link: 'https://quasar.dev'
  },
  {
    title: 'Github',
    caption: 'github.com/quasarframework',
    icon: 'code',
    link: 'https://github.com/quasarframework'
  },
  {
    title: 'Discord Chat Channel',
    caption: 'chat.quasar.dev',
    icon: 'chat',
    link: 'https://chat.quasar.dev'
  },
  {
    title: 'Forum',
    caption: 'forum.quasar.dev',
    icon: 'record_voice_over',
    link: 'https://forum.quasar.dev'
  },
  {
    title: 'Twitter',
    caption: '@quasarframework',
    icon: 'rss_feed',
    link: 'https://twitter.quasar.dev'
  },
  {
    title: 'Facebook',
    caption: '@QuasarFramework',
    icon: 'public',
    link: 'https://facebook.quasar.dev'
  },
  {
    title: 'Quasar Awesome',
    caption: 'Community Quasar projects',
    icon: 'favorite',
    link: 'https://awesome.quasar.dev'
  }
]

export default defineComponent({
  name: 'MainLayout',

  components: {
    // EssentialLink
    CustomList
  },

  setup () {
    const leftDrawerOpen = ref(false)

    // let content = require('src/content')
    // console.log(content)
    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      contentItems,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }
  }
})
</script>

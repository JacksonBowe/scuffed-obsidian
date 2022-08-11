<template>
  <q-layout view="hHh LpR lFf" class="">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title>
          Quasar App
        </q-toolbar-title>

        <div>Quasar v{{ $q.version }}</div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      dark
      :width="500"
      class="q-pl-xl"
    >
      <q-list class="q-ml-xl q-pl-xl q-pt-lg" :inner-width="100" :outer-width="50" >
        <q-item-label class=""
          header
        >
          Docs
        </q-item-label>

        <!-- <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        /> -->
        <custom-list
          v-for="child in contentItems.children"
          :key="child"

          :item="child"
        />
      </q-list>
    </q-drawer>
    <!-- <div class="bg-blue row">
      <div class="text-white bg-green">
        <span>Testffff<br><br><br><br><br><br>ffffffffffffffffffffffffffffffffffffffffffffffffffffff</span>
      </div> -->
      <q-page-container>
        <router-view />
      </q-page-container>
    <!-- </div> -->


  </q-layout>
</template>

<script>
import { defineComponent, ref } from 'vue'
// import EssentialLink from 'components/EssentialLink.vue'
import CustomList from 'src/components/CustomList.vue'
import contentItems from '../content/_map.json'

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

<template>
  <q-layout view="hHh LpR lFf" class="">

    <s-toolbar />
    <div class="row">
        <div class="col-2" style="max-width: 200px"></div>
        <div class="col-2 q-pt-xl">
            <q-list class="q-pt-lg"  dense >
                <q-item-label class="text-overline" header>
                	<span class="nav-header">Docs</span>
                </q-item-label>
                <custom-list v-for="child in contentItems.children" :key="child" :item="child" />
            </q-list>
        </div>
        <q-page-container class="col">
            <router-view />
        </q-page-container>
    </div>


  </q-layout>
</template>

<script>
import { defineComponent, ref, computed } from 'vue'
// import EssentialLink from 'components/EssentialLink.vue'
import CustomList from 'src/components/CustomList.vue'
import SToolbar from 'src/components/ScuffedToolbar.vue'
import contentItems from '../content/.map.json'
// import { fuse } from 'src/boot/fuse'



export default defineComponent({
  name: 'ContentLayout',

  components: {
    CustomList,
    SToolbar
  },

  setup () {

	// const openGraph = () => {
	// 	// TODO
	// 	console.log('opening graph')
	// }

    // const searchTerms = ref('')

    // const search = (val) => {
    //     searchTerms.value = val
    // }

    // const searchResults = computed(() => {
    //     // console.log(fuse.search(searchTerms.value))
    //     return fuse.search(searchTerms.value).map(
    //         (result) => {
    //             console.log({label: result.item.title, value: result.item.body})
    //             return {label: result.item.title.split('.')[0], value: result.item.body}
    //         }
    //     )
    // })

    // const searchSelection = ref(null)

    return {
    //   essentialLinks: linksList,
    //   leftDrawerOpen,
      contentItems,
	//   openGraph,
    //   searchTerms,
    //   search,
    //   searchResults,
    //   searchSelection
    }
  }
})
</script>


<style scoped>




</style>

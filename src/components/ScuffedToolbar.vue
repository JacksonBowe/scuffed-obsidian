<template>
  <q-header elevated dark class="bg-transparent">
      <q-toolbar class="row bg-transparent q-my-sm" dark>
        <div class="col-2" style="max-width:200px"></div>
        <div class="row col q-mr-md">
				<q-icon
				 name="hub"
				 round
				 size="sm"
				 class="graph-button"
				 @click="openGraph"
				/>


            <q-toolbar-title class="content-center flex">
            Mafia-SDG Docs
            </q-toolbar-title>


        </div>
            <q-select class="col q-mx-lg" dense rounded  outlined v-model="searchSelection" @input-value="search" use-input input-debounce="0" label="Search docs..." :options="searchResults || []" behaviour="menu" >
                <template v-slot:no-option>
                    <q-item>
                        <q-item-section class="text-grey">
                        No results
                        </q-item-section>
                    </q-item>
                </template>
                <template v-slot:option="scope">
                    <q-item v-bind="scope.itemProps" style="height: 200px">
                        <q-item-section avatar>
                            <q-item-label>{{ scope.opt.label }}</q-item-label>
                        </q-item-section>
                        <q-item-section>
                            <q-scroll-area class="fit">
                                <q-markdown :src="scope.opt.value" />
                            </q-scroll-area>
                            
                        </q-item-section>
                    </q-item>
                </template>
            </q-select>
        <div>
            Quasar v{{ $q.version }}
        </div>
		<div class="col" style="max-width: 200px">

		</div>
      </q-toolbar>
    </q-header>
</template>

<script>
import { fuse } from 'src/boot/fuse'
import { computed, ref } from 'vue'
import contentItems from '../content/.map.json'

export default {
  name: 'SToolbar',
  setup () {
        const leftDrawerOpen = ref(false)

        const openGraph = () => {
            // TODO
            console.log('opening graph')
        }

        const searchTerms = ref('')

        const search = (val) => {
            searchTerms.value = val
        }

        const searchResults = computed(() => {
            // console.log(fuse.search(searchTerms.value))
            return fuse.search(searchTerms.value).map(
                (result) => { 
                    console.log({label: result.item.title, value: result.item.body})
                    return {label: result.item.title.split('.')[0], value: result.item.body}
                }
            )
        })

        const searchSelection = ref(null)

        return {
        //   essentialLinks: linksList,
        //   leftDrawerOpen,
        contentItems,
        openGraph,
        searchTerms,
        search,
        searchResults,
        searchSelection
        }
    }
}
</script>

<style scoped >

.graph-button {
	color: #00FFFF;
	-webkit-transition: color 200ms linear;
    -ms-transition: color 200ms linear;
    transition: color 200ms linear;
}

.graph-button:hover{
	color: hotpink; /* TODO */
	cursor: pointer;

}

</style>

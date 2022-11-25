<template>
  <q-page padding>
    <div class="q-px-lg q-pb-md">
    <q-timeline color="primary" layout="comfortable">
      <q-timeline-entry
        title="Event Title"
      >
		<template v-slot:subtitle>
			<div class="bg-red">
				Test
			</div>
		</template>
        <div>
          <!-- Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. -->
			<q-expansion-item
			  expand-separator
			  label="Test Item"
			  caption="Test Caption"
			>
		</q-expansion-item>
		</div>
      </q-timeline-entry>

      <q-timeline-entry
        title="Event Title"
        subtitle="February 21, 1986"
        icon="delete"
      >
        <div>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </div>
      </q-timeline-entry>


    </q-timeline>
  </div>
  </q-page>
</template>

<script>
export default {
  // name: 'PageName',
}
</script>

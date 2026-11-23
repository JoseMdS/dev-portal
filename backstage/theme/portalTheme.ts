// Färgtema för dev-portalens Backstage-app.
// Inspirerat av marinblått, rött och vitt. Bara färger, inga loggor.
// Kopiera till packages/app/src/theme/portalTheme.ts i Backstage-appen.
import {
  createBaseThemeOptions,
  createUnifiedTheme,
  genPageTheme,
  palettes,
  shapes,
} from '@backstage/theme';

const marin = '#004170';
const marinMork = '#0A1F44';
const rod = '#DA291C';
const rodMork = '#A51D14';
const vit = '#FFFFFF';

const pageTheme = {
  home: genPageTheme({ colors: [marinMork, marin], shape: shapes.wave }),
  documentation: genPageTheme({ colors: [marin, marinMork], shape: shapes.wave2 }),
  tool: genPageTheme({ colors: [rodMork, rod], shape: shapes.round }),
  service: genPageTheme({ colors: [marinMork, rod], shape: shapes.wave }),
  website: genPageTheme({ colors: [marin, rod], shape: shapes.wave }),
  library: genPageTheme({ colors: [marinMork, marin], shape: shapes.wave2 }),
  other: genPageTheme({ colors: [marinMork, marin], shape: shapes.wave }),
  app: genPageTheme({ colors: [marin, rod], shape: shapes.wave }),
  apis: genPageTheme({ colors: [marinMork, rodMork], shape: shapes.wave2 }),
  card: genPageTheme({ colors: [marin, marinMork], shape: shapes.round }),
};

export const portalLightTheme = createUnifiedTheme({
  ...createBaseThemeOptions({
    palette: {
      ...palettes.light,
      primary: { main: marin },
      secondary: { main: rod },
      error: { main: rodMork },
      background: { default: '#F4F6FA', paper: vit },
      navigation: {
        background: marinMork,
        indicator: rod,
        color: '#C9D3E3',
        selectedColor: vit,
        navItem: { hoverBackground: marin },
        submenu: { background: marinMork },
      },
    },
  }),
  defaultPageTheme: 'home',
  pageTheme,
});

export const portalDarkTheme = createUnifiedTheme({
  ...createBaseThemeOptions({
    palette: {
      ...palettes.dark,
      primary: { main: '#5B9BD5' },
      secondary: { main: rod },
      background: { default: '#08152E', paper: marinMork },
      navigation: {
        background: '#050E20',
        indicator: rod,
        color: '#9FB0CC',
        selectedColor: vit,
        navItem: { hoverBackground: marin },
        submenu: { background: '#050E20' },
      },
    },
  }),
  defaultPageTheme: 'home',
  pageTheme,
});

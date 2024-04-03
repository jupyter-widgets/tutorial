"use strict";(self.webpackChunk_voila_dashboards_jupyterlab_preview=self.webpackChunk_voila_dashboards_jupyterlab_preview||[]).push([[97],{97:(e,t,a)=>{a.r(t),a.d(t,{CommandIDs:()=>b,default:()=>k});var o=a(271),n=a(583),r=a(979),l=a(46),i=a(14),s=a(854),d=a(413),c=a(880),v=a(526),h=a(840),p=a(918);const u=new c.LabIcon({name:"@voila-dashboards/jupyterlab-preview:voila",svgstr:'<svg width="308.95" height="308.95" data-name="Calque 1" version="1.1" viewBox="0 0 308.95 308.95" xmlns="http://www.w3.org/2000/svg">\n <defs>\n  <style>\n    [data-jp-theme-light=\'true\'] .jp-VoilaColor1 {fill:#268380;}\n    [data-jp-theme-light=\'true\'] .jp-VoilaColor2 {fill:#f8e14b;}\n    [data-jp-theme-light=\'false\'] .jp-VoilaColor1 {fill:#555454;}\n    [data-jp-theme-light=\'false\'] .jp-VoilaColor2 {fill:#f38c02;}\n  </style>\n </defs>\n <title>Voila</title>\n <g class="jp-icon3" transform="translate(-95.032 -95.527)">\n  <path class="jp-VoilaColor1" d="m391.05 343h-282.05a14 14 0 0 1 0-27.91h282.1a14 14 0 0 1 0 27.91z"/>\n  <path class="jp-VoilaColor2" d="m108.94 276.18a14 14 0 0 1-12.41-20.3l35.81-70.07c12.77-25.09 29.66-28.81 38.53-28.81s25.75 3.75 38.53 28.86l24.25 47.64c5.11 10.06 10.56 13.62 13.67 13.62s8.55-3.56 13.66-13.62l24.25-47.64c12.77-25.14 29.63-28.86 38.53-28.86 8.91 0 25.76 3.76 38.54 28.87a14 14 0 0 1-24.87 12.66c-5.11-10.06-10.56-13.62-13.67-13.62s-8.55 3.56-13.66 13.62l-24.25 47.64c-12.78 25.08-29.63 28.83-38.53 28.83s-25.76-3.75-38.54-28.87l-24.24-47.64c-5.12-10.06-10.56-13.62-13.67-13.62s-8.55 3.56-13.67 13.62l-35.82 70.09a14 14 0 0 1-12.44 7.6z"/>\n </g>\n</svg>\n'}),g=new v.Token("@voila-dashboards/jupyterlab-preview:IVoilaPreviewTracker");class m extends d.DocumentWidget{constructor(e){super(Object.assign(Object.assign({},e),{content:new n.IFrame({sandbox:["allow-same-origin","allow-scripts","allow-downloads","allow-modals","allow-popups"]})})),window.onmessage=e=>{var t,a,o,n,r;switch(null===(t=e.data)||void 0===t?void 0:t.level){case"debug":console.debug(...null===(a=e.data)||void 0===a?void 0:a.msg);break;case"info":console.info(...null===(o=e.data)||void 0===o?void 0:o.msg);break;case"warn":console.warn(...null===(n=e.data)||void 0===n?void 0:n.msg);break;case"error":console.error(...null===(r=e.data)||void 0===r?void 0:r.msg);break;default:console.log(e)}};const{getVoilaUrl:t,context:a,renderOnSave:o}=e;this.content.url=t(a.path),this.content.title.icon=u,this._renderOnSave=null!=o&&o,a.pathChanged.connect((()=>{this.content.url=t(a.path)}));const r=new n.ToolbarButton({icon:c.refreshIcon,tooltip:"Reload Preview",onClick:async()=>{try{await a.save()}catch(e){console.error(e)}this.reload()}}),l=n.ReactWidget.create(p.createElement("label",{className:"jp-VoilaPreview-renderOnSave"},p.createElement("input",{name:"renderOnSave",type:"checkbox",defaultChecked:o,onChange:e=>{this._renderOnSave=e.target.checked}}),"Render on Save"));this.toolbar.addItem("reload",r),a&&(this.toolbar.addItem("renderOnSave",l),a.ready.then((()=>{a.fileChanged.connect((()=>{this.renderOnSave&&this.reload()}))})))}dispose(){this.isDisposed||(super.dispose(),h.Signal.clearData(this))}reload(){const e=this.content.node.querySelector("iframe");e.contentWindow&&e.contentWindow.location.reload()}get renderOnSave(){return this._renderOnSave}set renderOnSave(e){this._renderOnSave=e}}class w extends d.ABCWidgetFactory{constructor(e,t){super(t),this.getVoilaUrl=e,this.defaultRenderOnSave=!1}createNewWidget(e){return new m({context:e,getVoilaUrl:this.getVoilaUrl,renderOnSave:this.defaultRenderOnSave})}}var b;!function(e){e.voilaRender="notebook:render-with-voila",e.voilaOpen="notebook:open-with-voila"}(b||(b={}));class f{constructor(e){this._commands=e}createNew(e){const t=new n.ToolbarButton({className:"voilaRender",tooltip:"Render with Voilà",icon:u,onClick:()=>{this._commands.execute(b.voilaRender)}});return e.toolbar.insertAfter("cellType","voilaRender",t),t}}const y={id:"@voila-dashboards/jupyterlab-preview:plugin",autoStart:!0,optional:[s.INotebookTracker,n.ICommandPalette,o.ILayoutRestorer,i.IMainMenu,r.ISettingRegistry],provides:g,activate:(e,t,a,o,r,i)=>{const s=new n.WidgetTracker({namespace:"voila-preview"});function d(a){var o;const n=null!==(o=null==t?void 0:t.currentWidget)&&void 0!==o?o:null;return!1!==a.activate&&n&&e.shell.activateById(n.id),n}function c(){return null!==(null==t?void 0:t.currentWidget)&&(null==t?void 0:t.currentWidget)===e.shell.currentWidget}function v(e){return`${l.PageConfig.getBaseUrl()}voila/render/${e}`}o&&o.restore(s,{command:"docmanager:open",args:e=>({path:e.context.path,factory:h.name}),name:e=>e.context.path,when:e.serviceManager.ready});const h=new w(v,{name:"Voila-preview",fileTypes:["notebook"],modelName:"notebook"});h.widgetCreated.connect(((e,t)=>{t.context.pathChanged.connect((()=>{s.save(t)})),s.add(t)}));const p=e=>{h.defaultRenderOnSave=e.get("renderOnSave").composite};i&&Promise.all([i.load(y.id),e.restored]).then((([e])=>{p(e),e.changed.connect(p)})).catch((e=>{console.error(e.message)})),e.docRegistry.addWidgetFactory(h);const{commands:u,docRegistry:g}=e;if(u.addCommand(b.voilaRender,{label:"Render Notebook with Voilà",execute:async e=>{const t=d(e);let a;if(t){a=t.context;try{await a.save()}catch(e){console.error(e)}u.execute("docmanager:open",{path:a.path,factory:"Voila-preview",options:{mode:"split-right"}})}},isEnabled:c}),u.addCommand(b.voilaOpen,{label:"Open with Voilà in New Browser Tab",execute:async e=>{const t=d(e);if(!t)return;try{await t.context.save()}catch(e){console.error(e)}const a=v(t.context.path);window.open(a)},isEnabled:c}),a){const e="Notebook Operations";[b.voilaRender,b.voilaOpen].forEach((t=>{a.addItem({command:t,category:e})}))}r&&r.viewMenu.addGroup([{command:b.voilaRender},{command:b.voilaOpen}],1e3);const m=new f(u);return g.addWidgetExtension("Notebook",m),s}},k=y}}]);
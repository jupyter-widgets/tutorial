(self["webpackChunk_jupyter_widgets_jupyterlab_sidecar"] = self["webpackChunk_jupyter_widgets_jupyterlab_sidecar"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __exportStar = (this && this.__exportStar) || function(m, exports) {
    for (var p in m) if (p !== "default" && !exports.hasOwnProperty(p)) __createBinding(exports, m, p);
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
__exportStar(__webpack_require__(/*! ./plugin */ "./lib/plugin.js"), exports);
__exportStar(__webpack_require__(/*! ./version */ "./lib/version.js"), exports);
__exportStar(__webpack_require__(/*! ./widget */ "./lib/widget.js"), exports);


/***/ }),

/***/ "./lib/plugin.js":
/*!***********************!*\
  !*** ./lib/plugin.js ***!
  \***********************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

"use strict";

// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
Object.defineProperty(exports, "__esModule", ({ value: true }));
const coreutils_1 = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils");
const base_1 = __webpack_require__(/*! @jupyter-widgets/base */ "webpack/sharing/consume/default/@jupyter-widgets/base");
const jupyterlab_manager_1 = __webpack_require__(/*! @jupyter-widgets/jupyterlab-manager */ "webpack/sharing/consume/default/@jupyter-widgets/jupyterlab-manager");
const widget_1 = __webpack_require__(/*! ./widget */ "./lib/widget.js");
const version_1 = __webpack_require__(/*! ./version */ "./lib/version.js");
__webpack_require__(/*! ../css/sidecar.css */ "./css/sidecar.css");
const EXTENSION_ID = '@jupyter-widgets/jupyterlab-sidecar';
const sidecarPlugin = {
    id: EXTENSION_ID,
    requires: [base_1.IJupyterWidgetRegistry],
    activate: activateWidgetExtension,
    autoStart: true
};
exports.default = sidecarPlugin;
/**
 * Activate the widget extension.
 */
function activateWidgetExtension(app, registry) {
    let SidecarView = class extends jupyterlab_manager_1.output.OutputView {
        render() {
            if (!this.model.rendered) {
                super.render();
                let w = this._outputView;
                w.addClass('jupyterlab-sidecar');
                w.addClass('jp-LinkedOutputView');
                w.title.label = this.model.get('title');
                w.title.closable = true;
                app.shell['_rightHandler'].sideBar.tabCloseRequested.connect((sender, tab) => {
                    tab.title.owner.dispose();
                });
                w.id = coreutils_1.UUID.uuid4();
                if (Object.keys(this.model.views).length > 1) {
                    w.node.style.display = 'none';
                    let key = Object.keys(this.model.views)[0];
                    this.model.views[key].then((v) => {
                        if (v instanceof jupyterlab_manager_1.output.OutputView) {
                            v._outputView.activate();
                        }
                    });
                }
                else {
                    let anchor = this.model.get('anchor') || 'right';
                    if (anchor === 'right') {
                        app.shell.add(w, 'right');
                    }
                    else {
                        app.shell.add(w, 'main', { mode: anchor });
                    }
                    app.shell.activateById(w.id);
                }
            }
        }
    };
    registry.registerWidget({
        name: '@jupyter-widgets/jupyterlab-sidecar',
        version: version_1.EXTENSION_SPEC_VERSION,
        exports: {
            // @ts-ignore: Why is this not compiling?
            SidecarModel: widget_1.SidecarModel, SidecarView
        }
    });
}


/***/ }),

/***/ "./lib/version.js":
/*!************************!*\
  !*** ./lib/version.js ***!
  \************************/
/***/ ((__unused_webpack_module, exports) => {

"use strict";

// Copyright (c) Project Jupyter.
// Distributed under the terms of the Modified BSD License.
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.EXTENSION_SPEC_VERSION = void 0;
/**
 * The version of the attribute spec that this package
 * implements. This is the value used in
 * _model_module_version/_view_module_version.
 *
 * Update this value when attributes are added/removed from
 * your models, or serialized format changes.
 */
exports.EXTENSION_SPEC_VERSION = '1.1.0';


/***/ }),

/***/ "./lib/widget.js":
/*!***********************!*\
  !*** ./lib/widget.js ***!
  \***********************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

"use strict";

// Copyright (c) Project Jupyter.
// Distributed under the terms of the Modified BSD License.
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SidecarModel = void 0;
const jupyterlab_manager_1 = __webpack_require__(/*! @jupyter-widgets/jupyterlab-manager */ "webpack/sharing/consume/default/@jupyter-widgets/jupyterlab-manager");
const version_1 = __webpack_require__(/*! ./version */ "./lib/version.js");
class SidecarModel extends jupyterlab_manager_1.output.OutputModel {
    defaults() {
        return Object.assign(Object.assign({}, super.defaults()), { _model_name: SidecarModel.model_name, _model_module: SidecarModel.model_module, _model_module_version: SidecarModel.model_module_version, _view_name: SidecarModel.view_name, _view_module: SidecarModel.view_module, _view_module_version: SidecarModel.view_module_version, title: 'Sidecar', anchor: 'right' });
    }
    initialize(attributes, options) {
        super.initialize(attributes, options);
        this.widget_manager.display_model(undefined, this, {});
    }
}
exports.SidecarModel = SidecarModel;
SidecarModel.model_name = 'SidecarModel';
SidecarModel.view_name = 'SidecarView';
SidecarModel.model_module = '@jupyter-widgets/jupyterlab-sidecar';
SidecarModel.view_module = '@jupyter-widgets/jupyterlab-sidecar';
SidecarModel.model_module_version = version_1.EXTENSION_SPEC_VERSION;
SidecarModel.view_module_version = version_1.EXTENSION_SPEC_VERSION;


/***/ }),

/***/ "./node_modules/css-loader/dist/cjs.js!./css/sidecar.css":
/*!***************************************************************!*\
  !*** ./node_modules/css-loader/dist/cjs.js!./css/sidecar.css ***!
  \***************************************************************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => __WEBPACK_DEFAULT_EXPORT__
/* harmony export */ });
/* harmony import */ var _node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/cssWithMappingToString.js */ "./node_modules/css-loader/dist/runtime/cssWithMappingToString.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/api.js */ "./node_modules/css-loader/dist/runtime/api.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__);
// Imports


var ___CSS_LOADER_EXPORT___ = _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default()((_node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0___default()));
// Module
___CSS_LOADER_EXPORT___.push([module.id, ".jupyterlab-sidecar {\n  background: var(--jp-layout-color0);\n  display: flex;\n}\n\n.jupyterlab-sidecar .jp-OutputPrompt.jp-OutputArea-prompt {\n  display: none;\n}\n\n.jupyterlab-sidecar > .jp-OutputArea-child {\n  flex: 1;\n}\n\n.jp-SideBar.jp-mod-right .p-TabBar-tabCloseIcon {\n  padding: 4px 0px 4px 4px;\n  background-size: 16px;\n  height: 16px;\n  width: 16px;\n  background-image: var(--jp-icon-close);\n  background-position: center;\n  background-repeat: no-repeat;\n  align-self: center;\n}\n\n.jp-SideBar.jp-mod-right .p-TabBar-tabCloseIcon:hover {\n  background-size: 16px;\n  background-image: var(--jp-icon-inverse-close-circle);\n}\n", "",{"version":3,"sources":["webpack://./css/sidecar.css"],"names":[],"mappings":"AAAA;EACE,mCAAmC;EACnC,aAAa;AACf;;AAEA;EACE,aAAa;AACf;;AAEA;EACE,OAAO;AACT;;AAEA;EACE,wBAAwB;EACxB,qBAAqB;EACrB,YAAY;EACZ,WAAW;EACX,sCAAsC;EACtC,2BAA2B;EAC3B,4BAA4B;EAC5B,kBAAkB;AACpB;;AAEA;EACE,qBAAqB;EACrB,qDAAqD;AACvD","sourcesContent":[".jupyterlab-sidecar {\n  background: var(--jp-layout-color0);\n  display: flex;\n}\n\n.jupyterlab-sidecar .jp-OutputPrompt.jp-OutputArea-prompt {\n  display: none;\n}\n\n.jupyterlab-sidecar > .jp-OutputArea-child {\n  flex: 1;\n}\n\n.jp-SideBar.jp-mod-right .p-TabBar-tabCloseIcon {\n  padding: 4px 0px 4px 4px;\n  background-size: 16px;\n  height: 16px;\n  width: 16px;\n  background-image: var(--jp-icon-close);\n  background-position: center;\n  background-repeat: no-repeat;\n  align-self: center;\n}\n\n.jp-SideBar.jp-mod-right .p-TabBar-tabCloseIcon:hover {\n  background-size: 16px;\n  background-image: var(--jp-icon-inverse-close-circle);\n}\n"],"sourceRoot":""}]);
// Exports
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (___CSS_LOADER_EXPORT___);


/***/ }),

/***/ "./css/sidecar.css":
/*!*************************!*\
  !*** ./css/sidecar.css ***!
  \*************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => __WEBPACK_DEFAULT_EXPORT__
/* harmony export */ });
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js */ "./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_cjs_js_sidecar_css__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! !!../node_modules/css-loader/dist/cjs.js!./sidecar.css */ "./node_modules/css-loader/dist/cjs.js!./css/sidecar.css");

            

var options = {};

options.insert = "head";
options.singleton = false;

var update = _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default()(_node_modules_css_loader_dist_cjs_js_sidecar_css__WEBPACK_IMPORTED_MODULE_1__.default, options);



/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (_node_modules_css_loader_dist_cjs_js_sidecar_css__WEBPACK_IMPORTED_MODULE_1__.default.locals || {});

/***/ })

}]);
//# sourceMappingURL=lib_index_js.9091bc546a51616ca372.js.map